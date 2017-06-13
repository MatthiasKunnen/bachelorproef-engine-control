from pyudev import Context, Monitor, Device
from pyudev.glib import MonitorObserver


class StorageMonitor:
    callbacks = []

    def __init__(self):
        """
        Start listening for storage events.
        """

        context = Context()
        monitor = Monitor.from_netlink(context)

        monitor.filter_by(subsystem='block')
        monitor_observer = MonitorObserver(monitor)

        monitor_observer.connect('device-event', self._device_event)
        monitor.start()

    def add_usb_insert_notifier(self, callback):
        # type: (function) -> None
        """
        The supplied callback will be called when a USB device with a partition
        is connected. The first argument given will be the device's block and
        the device object.
        """

        self.callbacks.append(callback)

    def _device_event(self, observer, device):
        # type: (MonitorObserver, Device) -> None
        """
        Internal function which is called when a block event occurred.
        """

        if device.action == 'add' and device.device_type == 'partition':
            for c in self.callbacks:
                c(device.device_node, device)
