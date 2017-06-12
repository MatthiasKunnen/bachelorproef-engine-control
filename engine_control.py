import RPi.GPIO as GPIO
from enum import IntEnum


class EngineControl:
    class State(IntEnum):
        OFF = 0
        CLOCKWISE = 1
        COUNTERCLOCKWISE = 2

    def __init__(self, pin1, pin2):
        # type: (float, float) -> None
        """
        Create a new EngineControl object with two GPIO pins.
        Uses GPIO.BOARD mode.
        """

        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)

    def set_state(self, state):
        # type: (int) -> None
        """Sets a new state for the engine."""

        if state == self.State.OFF:
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, False)
        elif state == self.State.CLOCKWISE:
            GPIO.output(self.pin2, False)
            GPIO.output(self.pin1, True)
        elif state == self.State.COUNTERCLOCKWISE:
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, True)
