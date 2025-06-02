import unittest
from unittest.mock import patch
from src.clients.AppleMusicClient import AppleMusicClient
from utils.TestData import TestData

ARTIST = "Artist Name"
SONG_TITLE = "The Song Title"
NOW_PLAYING = 1

class TestAppleMusicClient(unittest.TestCase):
    def setUp(self):
        self.appleMusicClient = AppleMusicClient()

    @patch('subprocess.run')
    def testGetCurrentlyPlayingSong(self, mock_run):
        mock_run.return_value.stdout = TestData.create_now_playing_message(ARTIST, SONG_TITLE, NOW_PLAYING)
        mock_run.return_value.returncode = 0

        metadata = self.appleMusicClient.get_current_playing_song()

        mock_run.assert_called_once_with(("osascript", "/tmp/now-playing.scpt"), capture_output=True, text=True)
        self.assertEqual(ARTIST, metadata.get_currently_playing_artist())
        self.assertEqual(SONG_TITLE, metadata.get_currently_playing_title())
        self.assertEqual(NOW_PLAYING, metadata.get_currently_playing_status())

suite = unittest.TestLoader().loadTestsFromTestCase(TestAppleMusicClient)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)