from models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata
from models.MarqueeMessage import MarqueeMessage
from models.MarqueeMessageColor import MarqueeMessageColor
from models.MarqueeMessageFont import MarqueeMessageFont
from models.MarqueeMessageMode import MarqueeMessageMode
from models.MarqueeMessages import MarqueeMessages


class TestData:
    """
    TestData is a class that provides various test data for unit tests.
    It includes methods to create instances of MarqueeMessage and other related classes.
    """

    @staticmethod
    def createMarqueeMessage(text: str = "") -> MarqueeMessage:
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
    def createMarqueeMessages(marqueeMessage: MarqueeMessage) -> MarqueeMessages:
        """
        Helper method to create a MarqueeMessages object.
        :param MarqueeMessage: The MarqueeMessage for the MarqueeMessages.
        :return: A MarqueeMessages object.
        """
        messages = MarqueeMessages()
        messages.add_message(marqueeMessage)
        return messages
    
    @staticmethod
    def createArtistAndTitleString(artist: str = "Test Artist", title: str = "Test Title") -> str:
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
    def createAppleMusicNowPlayingMetadata(artist: str = "Test Artist", title: str = "Test Title", nowPlaying: int = 1) -> AppleMusicNowPlayingMetadata:
        """
        Helper method to create a dictionary with Apple Music Now Playing data.
        :param artist: The artist name.
        :param title: The song title.
        :param nowPlaying: If audio is currently being played.
        :return: A dict object with Apple Music Now Playing data.
        """
        return AppleMusicNowPlayingMetadata(artist, title, nowPlaying)
    
    @staticmethod
    def createNowPlayingMessage(artist: str = "Test Artist", title: str = "Test Title", nowPlaying: int = 1) -> str:
        """
        Helper method to create a NowPlayingMessage object.
        :param artist: The artist name.
        :param title: The song title.
        :param nowPlaying: If audio is currently being played.
        :return: A str object with Now Playing data.
        """
        nowPlayingResult = "{"
        f"  kMRMediaRemoteNowPlayingInfoAlbum = \"Test - EP\";"
        f"  kMRMediaRemoteNowPlayingInfoAlbumiTunesStoreAdamIdentifier = 1680977975;"
        f"  kMRMediaRemoteNowPlayingInfoArtist = {artist};"
        f"  kMRMediaRemoteNowPlayingInfoArtistiTunesStoreAdamIdentifier = 718366539;"
        f"  kMRMediaRemoteNowPlayingInfoArtworkIdentifier = dfdaba18baa070a9250d86e96590d370d892e598bcee8990307785838336c083;"
        f"  kMRMediaRemoteNowPlayingInfoArtworkMIMEType = \"image/png\";"
        f"  kMRMediaRemoteNowPlayingInfoComposer = \"Test Composer\";"
        f"  kMRMediaRemoteNowPlayingInfoContentItemIdentifier = 1680977980;"
        f"  kMRMediaRemoteNowPlayingInfoDuration = \"179.052\";"
        f"  kMRMediaRemoteNowPlayingInfoElapsedTime = \"14.912\";"
        f"  kMRMediaRemoteNowPlayingInfoGenre = Rock;"
        f"  kMRMediaRemoteNowPlayingInfoIsMusicApp = 1;"
        f"  kMRMediaRemoteNowPlayingInfoMediaType = MRMediaRemoteMediaTypeMusic;"
        f"  kMRMediaRemoteNowPlayingInfoPlaybackRate = {nowPlaying};"
        f"  kMRMediaRemoteNowPlayingInfoQueueIndex = 0;"
        f"  kMRMediaRemoteNowPlayingInfoRepeatMode = 3;"
        f"  kMRMediaRemoteNowPlayingInfoShuffleMode = 1;"
        f"  kMRMediaRemoteNowPlayingInfoTimestamp = \"2025-04-04 22:44:35 +0000\";"
        f"  kMRMediaRemoteNowPlayingInfoTitle = \"{title}\";"
        f"  kMRMediaRemoteNowPlayingInfoTotalQueueCount = 20;"
        f"  kMRMediaRemoteNowPlayingInfoTotalTrackCount = 5;"
        f"  kMRMediaRemoteNowPlayingInfoTrackNumber = 1;"
        f"  kMRMediaRemoteNowPlayingInfoUniqueIdentifier = 8232658841596513572;"
        f"  kMRMediaRemoteNowPlayingInfoiTunesStoreIdentifier = 1680977980;"
        f"  kMRMediaRemoteNowPlayingInfoiTunesStoreSubscriptionAdamIdentifier = 1680977980;"
        "}"
        return nowPlayingResult