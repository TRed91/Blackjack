from enum import Enum

class PlayerResult(Enum):
    BUST = "bust"
    BELOW = "below 21"
    ON21 = "21"
    NONE = "none"