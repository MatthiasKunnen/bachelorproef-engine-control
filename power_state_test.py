from default_engine_control import get_engine_control
from engine_control import EngineControl
from sys import stdout

engineControl = get_engine_control()

while True:
    stdout.write("Give in next power state: ")
    inp = raw_input()
    if inp == "":
        break

    engineControl.set_state(int(inp))

engineControl.set_state(EngineControl.State.OFF)
