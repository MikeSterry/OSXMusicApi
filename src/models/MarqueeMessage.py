import json

from src.models.MarqueeMessageColor import MarqueeMessageColor
from src.models.MarqueeMessageFont import MarqueeMessageFont
from src.models.MarqueeMessageMode import MarqueeMessageMode


class MarqueeMessage:
    def __init__(self, text: str = "",
                 color: MarqueeMessageColor = MarqueeMessageColor.AUTOCOLOR,
                 font: MarqueeMessageFont = MarqueeMessageFont.SEVEN_HIGH_FANCY,
                 mode: MarqueeMessageMode = MarqueeMessageMode.ROLL_LEFT):
        self.text = text
        self.color = color
        self.font = font
        self.mode = mode

    def __repr__(self):
        return json.dumps(self.get_marquee_message())

    def get_marquee_message(self):
        return {
            "text": self.text,
            "color": self.color.name,
            "font": self.font.name,
            "mode": self.mode.name
        }

    def set_marquee_message(self, text: str, color: MarqueeMessageColor, font: MarqueeMessageFont, mode: MarqueeMessageMode) -> None:
        """
        Sets the marquee message
        :param text: The text of the message
        :param color: The color of the message
        :param font: The font of the message
        :param mode: The mode of the message
        """
        self.text = text
        self.color = color
        self.font = font
        self.mode = mode

    def create_marquee_message_from_artist_and_song_title(self, artist: str, songTitle: str) -> dict:
        """
        Creates a marquee message from the artist and song title
        :param artist: The artist name
        :param songTitle: The song title
        :return: The marquee message
        """
        # Format the message
        message = self.convert_artist_title_to_marquee_message(artist, songTitle)
        # Set the message
        self.text = message
        self.color = MarqueeMessageColor.AUTOCOLOR
        self.font = MarqueeMessageFont.SEVEN_HIGH_FANCY
        self.mode = MarqueeMessageMode.ROLL_LEFT
        return self.get_marquee_message()

    def convert_artist_title_to_marquee_message(self, artist: str, songTitle: str) -> str:
        """
        Converts the artist and song title to a marquee message
        :param artist: The artist name
        :param songTitle: The song title
        :return: The marquee message
        """
        # Format the message
        spacer = "###"
        return (
            f"{spacer}{MarqueeMessageColor.RAINBOW_1}{spacer}{artist}"
            f"{spacer}{MarqueeMessageColor.AMBER}{spacer} - {spacer}"
            f"{MarqueeMessageColor.RAINBOW_2}{spacer}{songTitle}"
        )

    def extract_artist_and_song_title_from_marquee_message(self) -> tuple:
        """
        Extracts the artist and song title from the marquee message
        :return: The artist and song title
        """
        # Split the message
        parts = self.text.split("###")
        # Get the artist and song title
        artist = parts[2]
        song_title = parts[6]
        return artist, song_title