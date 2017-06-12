from engine_control import EngineControl


def get_engine_control():
    # type: () -> EngineControl
    """Get the default engine control. Change this if you have a different setup."""

    return EngineControl(12, 11)
