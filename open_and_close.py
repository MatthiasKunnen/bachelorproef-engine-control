import sys
import time
from default_engine_control import get_engine_control
from engine_control import EngineControl

runTime = 3
keepOpen = 3

if len(sys.argv) == 2:
    runTime = float(sys.argv[1])

if len(sys.argv) == 3:
    keepOpen = float(sys.argv[2])

engineControl = get_engine_control()


def open_and_close(engine_control, run_time, delay):
    # type: (EngineControl, float, float) -> None
    """
    Run engine in clockwise direction for :run_time, waits :delay, and runs
    in counter clockwise direction for :run_time
    """

    engine_control.set_state(EngineControl.State.CLOCKWISE)
    time.sleep(run_time)
    engine_control.set_state(EngineControl.State.OFF)
    time.sleep(delay)
    engine_control.set_state(EngineControl.State.COUNTERCLOCKWISE)
    time.sleep(run_time)
    engine_control.set_state(EngineControl.State.OFF)


open_and_close(engineControl, runTime, keepOpen)
