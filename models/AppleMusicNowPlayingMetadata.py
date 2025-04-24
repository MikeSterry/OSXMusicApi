import json


class AppleMusicNowPlayingMetadata:
    """
    A class to interact with the Apple Music Now Playing.
    """
    def __init__(self, artist: str = "", title: str = "", currently_playing: int = 0):
        """
        Initializes the AppleMusicNowPlayingMetadata.
        """
        self.artist = artist
        self.title = title
        self.currently_playing = currently_playing

    def __repr__(self):
        return json.dumps(self.__dict__)

    def get_currently_playing_metadata(self):
        """
        Returns the currently playing metadata.
        :return: The currently playing metadata
        """
        return {
            "artist": self.artist,
            "title": self.title,
            "currently_playing": self.currently_playing
        }
    
    def get_currently_playing_artist(self):
        """
        Returns the currently playing artist.
        :return: The currently playing artist
        """
        return self.artist
    
    def get_currently_playing_title(self):
        """
        Returns the currently playing title.
        :return: The currently playing title
        """
        return self.title
    
    def get_currently_playing_status(self):
        """
        Returns the currently playing status.
        :return: The currently playing status
        """
        return self.currently_playing
