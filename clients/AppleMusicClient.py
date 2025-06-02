import subprocess
from configparser import ConfigParser

from models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata

"""
Constants for the Apple Music Now Playing.

Output example:
Title: Rocksmith 2014 - DLC - Guitar - Disturbed "The Night"
Album:
Artist: Riff Repeater
AppName: Safari
"""
NOW_PLAYING_INFO_ARTIST = "Artist"
NOW_PLAYING_INFO_TITLE = "Title"
NOW_PLAYING_ALBUM = "Album"
NOW_PLAYING_APP = "AppName"
SCRIPT_NAME = "now-playing.scpt"


class AppleMusicClient:
    """
    A class to interact with the Apple Music Now Playing.
    """

    def __init__(self, config_file='config.ini'):
        """
        Initializes the AppleMusicClient.
        """
        self.config = ConfigParser()
        self.config.read(config_file)
        self.script_location = self.config.get('AppleMusicNowPlaying', 'script_location').rstrip('/')

    """
        Gets the current playing song from Apple Music.
        :return: The current playing song
    """
    def get_current_playing_song(self) -> AppleMusicNowPlayingMetadata:
        command = "osascript", f"{self.script_location}/{SCRIPT_NAME}"
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to execute script: {result.stderr.strip()}")

        return self._parse_r_media_remote_now_playing_info(result.stdout)

    """
        Parses the output of the nowplaying-cli command.
        :param str: The output of the nowplaying-cli command
        :return: The parsed now playing info
    """
    def _parse_r_media_remote_now_playing_info(self, now_playing_info: str) -> AppleMusicNowPlayingMetadata:
        artist = ""
        title = ""
        album = ""
        now_playing_app = ""
        currently_playing = 0
        now_playing_dict = self._create_dictionary_from_output(now_playing_info)
        for key, value in now_playing_dict.items():
            try:
                if key == NOW_PLAYING_INFO_ARTIST:
                    artist = self._strip_characters(value)
                if key == NOW_PLAYING_INFO_TITLE:
                    title = self._strip_characters(value)
                    currently_playing = 1
                if key == NOW_PLAYING_ALBUM:
                    album = self._strip_characters(value)
                if key == NOW_PLAYING_APP:
                    now_playing_app = self._strip_characters(value)
            except ValueError:
                pass

        return self._create_apple_music_now_playing_metadata(artist, title, currently_playing)

    def _create_apple_music_now_playing_metadata(self, artist: str, title: str, currently_playing: int) -> AppleMusicNowPlayingMetadata:
        """
        Creates an instance of AppleMusicNowPlayingMetadata.
        :param artist: The artist name
        :param title: The song title
        :param currently_playing: The currently playing status
        :return: The AppleMusicNowPlayingMetadata instance
        """
        return AppleMusicNowPlayingMetadata(artist, title, currently_playing)

    def _strip_characters(self, text: str) -> str:
        """
        Strips the characters from the text.
        :param text: The text to strip
        :return: The stripped text
        """
        return text.rstrip(';').replace("\"", "")

    def _create_dictionary_from_output(self, now_playing_info: str) -> dict:
        """
        Creates a dictionary from the output of the nowplaying-cli command.
        :param now_playing_info: The output of the nowplaying-cli command
        :return: The dictionary
        """
        result = {}
        for line in now_playing_info.splitlines():
            try:
                key, value = line.lstrip().split(': ')
                result[key] = self._strip_characters(value)
            except ValueError:
                pass
        return result
