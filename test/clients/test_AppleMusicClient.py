import unittest
import subprocess
from unittest.mock import patch
from clients.AppleMusicClient import AppleMusicClient
from test.utils.TestData import TestData

ARTIST = "Artist Name"
SONG_TITLE = "The Song Title"
NOW_PLAYING = 1

class TestAppleMusicClient(unittest.TestCase):
    def setUp(self):
        self.appleMusicClient = AppleMusicClient()

    @patch('subprocess.run')
    def testGetCurrentlyPlayingSong(self, mock_run):
        print(f"Test Data: {TestData.createNowPlayingMessage(ARTIST, SONG_TITLE, NOW_PLAYING)}")
        mock_run.return_value.stdout = TestData.createNowPlayingMessage(ARTIST, SONG_TITLE, NOW_PLAYING)
        mock_run.return_value.returncode = 0

        metadata = self.appleMusicClient.get_current_playing_song()
        print(f"metadata:{metadata.get_currently_playing_metadata}")

        mock_run.assert_called_once_with(("/usr/local/bin/nowplaying-cli", "get-raw"), capture_output=True, text=True)
        self.assertEqual(metadata.get_currently_playing_artist, ARTIST)
        self.assertEqual(metadata.get_currently_playing_title, SONG_TITLE)
        self.assertEqual(metadata.get_currently_playing_status, NOW_PLAYING)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAppleMusicClient)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)