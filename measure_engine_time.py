import time
from default_engine_control import get_engine_control
from engine_control import EngineControl
from sys import stdin
from sys import stdout

while True:
    stdout.write("Enter {0} to start clockwise test and {1} to start counterclockwise: "
                 .format(EngineControl.State.CLOCKWISE.value,
                         EngineControl.State.COUNTERCLOCKWISE.value))
    choice = stdin.readline()
    if choice == '':
        break

    desiredState = int(choice)

    engineControl = get_engine_control()
    engineControl.set_state(desiredState)
    start = time.time()
    stdout.write("Hit enter to stop")
    stdin.readline()
    end = time.time()
    engineControl.set_state(EngineControl.State.OFF)

    print("The elapsed time in seconds is: {0}".format(end - start))
