from enum import IntEnum, auto


class ExitState(IntEnum):
    EXIT = auto()
    CONTINUE = auto()
    RESTART = auto()
