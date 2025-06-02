from enum import StrEnum, auto


class MarqueeMessageMode(StrEnum):
    """
    Enum for Marquee Message Modes.
    """
    ROTATE = auto()
    HOLD = auto()
    ROLL_UP = auto()
    ROLL_DOWN = auto()
    ROLL_LEFT = auto()
    ROLL_RIGHT = auto()
    WIPE_UP = auto()
    WIPE_DOWN = auto()
    WIPE_LEFT = auto()
    WIPE_RIGHT = auto()
    SCROLL = auto()
    ROLL_IN = auto()
    ROLL_OUT = auto()
    WIPE_IN = auto()
    WIPE_OUT = auto()
    TWINKLE = auto()
    SPARKLE = auto()
    SNOW = auto()
    INTERLOCK = auto()
    SWITCH = auto()
    SPRAY = auto()
    STARBURST = auto()
    WELCOME = auto()
    SLOT_MACHINE = auto()
    THANK_YOU = auto()
    NO_SMOKING = auto()
    DONT_DRINK_DRIVE = auto()
    RUNNING_ANIMAL = auto()
    FIREWORKS = auto()
    TURBO_CAR = auto()
    FLASH = auto()
    AUTO_MODE = auto()
    COMPRESSED_ROTATE = auto()
    EXPLODE = auto()
    CLOCK = auto()
    NEWS_FLASH = auto()
    TRUMPET_ANIMATION = auto()
    FISH_ANIMATION = auto()
    BALLOON_ANIMATION = auto()
    CHERRY_BOMB = auto()

    def __str__(self):
        return self.value
