import time
from pygame import mixer


def play_sound(path, volume=1.0, wait=False):
    # type: (str, float, bool) -> None
    """
    Plays a sound file at a certain volume. If wait is true, the thread will
    sleep until the sound file finished playing. The volume is a value
    between 0.0 and 1.0.
    """

    mixer.init()
    mixer.music.load(path)
    mixer.music.set_volume(volume)
    mixer.music.play()
    while not wait and mixer.music.get_busy():
        time.sleep(0.1)
