import time
from default_engine_control import get_engine_control
from engine_control import EngineControl


def extend_parser(parser):
    parser.add_argument('-t', '--time', type=float, default=1,
                        help='Time in seconds that the engine needs to run to '
                             'travel in one direction.')
    parser.add_argument('-d', '--delay', type=float, default=3,
                        help='Time in seconds until starting the travel in the '
                             'opposite direction')


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


if __name__ == '__main__':
    import argparse as ap

    p = ap.ArgumentParser(description='Run engine clockwise. Wait. Run the '
                                      'engine counterclockwise')
    extend_parser(p)
    args, leftovers = p.parse_known_args()
    runTime = args.time
    keepOpen = args.delay
    engineControl = get_engine_control()
    open_and_close(engineControl, runTime, keepOpen)
