import argparse as ap
import glib
import os
import time

from datetime import datetime
from detect_storage_insert import StorageMonitor
from mount import get_block_mount_point
from mount import mount_block
from mount import unmount
from pyudev import Device

parser = ap.ArgumentParser(description='Access listener')
parser.add_argument('-v', '--verbose', help='increase output verbosity',
                    action='store_true')
parser.add_argument('--wait-for-auto-mount', type=float,
                    help='Signals that auto mounting is active and that the '
                         'script should wait x seconds before mounting.')
args, leftovers = parser.parse_known_args()
waitForAutoMount = args.wait_for_auto_mount


def print_verbose(text, prepend_time=True):
    # type: (str, bool) -> None
    """
    Prints the supplied text if verbosity is turned on. Prefixes the output
    with the current time if prepend_time is true
    """

    if args.verbose:
        prefix = ''

        if prepend_time:
            prefix = datetime.now().time().isoformat() + ': '

        print(prefix + text)


def notify_callback(block, device):
    # type: (str, Device) -> None
    """This callback is called when a new partition was added."""

    print_verbose('New block added: {0}'.format(block))

    should_unmount = True

    if waitForAutoMount is not None:
        time.sleep(waitForAutoMount)  # Wait some time for auto mounting to occur
        mount_result = get_block_mount_point(block)
        mount_point = mount_result[0]
        should_unmount = not mount_result[1]
    else:
        mount_point = mount_block(block)

    print_verbose('Mounted on {0}'.format(mount_point))
    nonce_path = os.path.join(mount_point, 'nonce')
    nonce_signature_path = os.path.join(mount_point, 'nonce.sig')

    if not os.path.isfile(nonce_path) or not os.path.isfile(nonce_signature_path):
        print('USB device does not contain a nonce nor signature.')
    # TODO: commit to server

    if should_unmount:
        print_verbose('Unmounting {0}'.format(mount_point))
        unmount(mount_point)
        print_verbose('Unmounted {0}'.format(mount_point))


storageMonitor = StorageMonitor()
storageMonitor.add_usb_insert_notifier(notify_callback)

glib.MainLoop().run()
