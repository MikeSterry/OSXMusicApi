from enum import StrEnum, auto


class MarqueeMessageFont(StrEnum):
    """
    Enum for Marquee Message Fonts.
    """
    FIVE_HIGH_STD = auto()
    SEVEN_HIGH_STD = auto()
    SEVEN_HIGH_FANCY = auto()

    def __str__(self):
        return self.value
