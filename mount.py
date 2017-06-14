import os
import subprocess
import tempfile


def _mount(source, target):
    # type: (str, str) -> None
    """
    Mounts the source at the target mount point.
    Raises an OSError if the mount fails.
    """

    mount_options = ['mount', source, target]

    process = subprocess.Popen(mount_options, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode > 0:
        raise OSError(err)


def unmount(mount_point):
    # type: (str) -> None
    """
    Unmounts the mount point and removes the mount point.
    Raises an OSError if the unmount fails.
    """

    p = subprocess.Popen(['umount', mount_point], stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode > 0:
        raise OSError(err)
    else:
        os.rmdir(mount_point)


def find_block_mount_point(block):
    # type: (str) -> str
    """
    Checks if a block is mounted.
    Returns the mount point of the block or None if the block is not mounted.
    """

    try:
        return subprocess.check_output([
            'findmnt',
            '-o',
            'TARGET',
            '-nS',
            block
        ]).strip()
    except subprocess.CalledProcessError as ex:
        return None


def get_block_mount_point(block):
    # type: (str) -> Tuple[str, bool]
    """
    Get the current mount point or mounts the block and then returns
    the mount point and a boolean value. The latter is true when the
    block was already mounted, false otherwise.
    """

    mount_point = find_block_mount_point(block)
    if mount_point is None:
        return mount_block(block), False
    else:
        return mount_point, True


def mount_block(block):
    # type: (str) -> str
    """Mounts the block on a temporary directory and returns the directory."""

    dir_path = tempfile.mkdtemp(prefix='mount-')
    _mount(block, dir_path)

    return dir_path
