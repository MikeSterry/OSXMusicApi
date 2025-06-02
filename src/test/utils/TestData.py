from src.models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata
from src.models.MarqueeMessage import MarqueeMessage
from src.models.MarqueeMessageColor import MarqueeMessageColor
from src.models.MarqueeMessageFont import MarqueeMessageFont
from src.models.MarqueeMessageMode import MarqueeMessageMode
from src.models.MarqueeMessages import MarqueeMessages


class TestData:
    """
    TestData is a class that provides various test data for unit tests.
    It includes methods to create instances of MarqueeMessage and other related classes.
    """

    @staticmethod
    def create_marquee_message(text: str = "") -> MarqueeMessage:
        """
        Helper method to create a MarqueeMessage object.
        :param text: The text for the MarqueeMessage.
        :return: A MarqueeMessage object.
        """
        message = MarqueeMessage()
        message.text = text
        message.color = MarqueeMessageColor.AUTOCOLOR
        message.font = MarqueeMessageFont.SEVEN_HIGH_FANCY
        message.mode = MarqueeMessageMode.ROLL_LEFT
        return message

    @staticmethod
    def create_marquee_messages(marqueeMessage: MarqueeMessage) -> MarqueeMessages:
        """
        Helper method to create a MarqueeMessages object.
        :param MarqueeMessage: The MarqueeMessage for the MarqueeMessages.
        :return: A MarqueeMessages object.
        """
        messages = MarqueeMessages()
        messages.add_message(marqueeMessage)
        return messages

    @staticmethod
    def create_artist_and_title_string(artist: str = "Test Artist", title: str = "Test Title") -> str:
        """
        Helper method to create a string from artist and title.
        :param artist: The artist name.
        :param title: The song title.
        :return: A str object with the artist and title.
        """
        spacer = "###"
        message = (
            f"{spacer}{MarqueeMessageColor.RAINBOW_1}{spacer}{artist}"
            f"{spacer}{MarqueeMessageColor.AMBER}{spacer} - {spacer}"
            f"{MarqueeMessageColor.RAINBOW_2}{spacer}{title}"
        )
        return message

    @staticmethod
    def create_apple_music_now_playing_metadata(artist: str = "Test Artist", title: str = "Test Title", now_playing: int = 1) -> AppleMusicNowPlayingMetadata:
        """
        Helper method to create a dictionary with Apple Music Now Playing data.
        :param artist: The artist name.
        :param title: The song title.
        :param now_playing: If audio is currently being played.
        :return: A dict object with Apple Music Now Playing data.
        """
        return AppleMusicNowPlayingMetadata(artist, title, now_playing)

    @staticmethod
    def create_now_playing_message(artist: str = "Test Artist", title: str = "Test Title", now_playing: int = 1) -> str:
        """
        Helper method to create a NowPlayingMessage object.
        :param artist: The artist name.
        :param title: The song title.
        :param now_playing: If audio is currently being played.
        :return: A str object with Now Playing data.
        """
        now_playing_result  = f"""Title: {title}
            Album: Test - EP
            Artist: {artist}
            AppName: Safari"""
        return now_playing_result
