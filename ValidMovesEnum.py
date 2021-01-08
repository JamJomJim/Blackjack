from enum import Enum


class Move(Enum):
    STAND = "stand"
    HIT = "hit"
    SPLIT = "split"
    DOUBLE = "double"
    SURRENDER = "surrender"
