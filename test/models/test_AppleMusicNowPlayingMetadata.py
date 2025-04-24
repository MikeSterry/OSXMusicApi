import unittest
from test.utils.TestData import TestData

from models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata

ARTIST = "Artist Name"
SONG_TITLE = "The Song Title"
NOW_PLAYING = 1

class TestAppleMusicNowPlayingMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = TestData.createAppleMusicNowPlayingMetadata(ARTIST, SONG_TITLE, NOW_PLAYING)

    def testGetArtist(self):
        self.assertEqual(self.metadata.get_currently_playing_artist(), ARTIST)

    def testGetSongTitle(self):
        self.assertEqual(self.metadata.get_currently_playing_title(), SONG_TITLE)

    def testGetNowPlaying(self):
        self.assertEqual(self.metadata.get_currently_playing_status(), NOW_PLAYING)

    def testGetBody(self):
        expected = {
            "artist": ARTIST,
            "title": SONG_TITLE,
            "currently_playing": NOW_PLAYING
        }
        self.assertEqual(self.metadata.get_currently_playing_metadata(), expected)