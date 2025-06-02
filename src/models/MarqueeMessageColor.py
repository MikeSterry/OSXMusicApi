from enum import StrEnum, auto


class MarqueeMessageColor(StrEnum):
    """
    Enum for Marquee Message Colors.
    """
    RED = auto()
    GREEN = auto()
    AMBER = auto()
    RAINBOW_1 = auto()
    RAINBOW_2 = auto()
    COLOR_MIX = auto()
    AUTOCOLOR = auto()

    def __str__(self):
        return self.value
