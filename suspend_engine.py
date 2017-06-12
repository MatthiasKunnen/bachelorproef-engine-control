from default_engine_control import get_engine_control
from engine_control import EngineControl

engineControl = get_engine_control()
engineControl.set_state(EngineControl.State.OFF)
