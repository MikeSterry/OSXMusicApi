import unittest
from test.utils.TestData import TestData

from models.MarqueeMessage import MarqueeMessage
from models.MarqueeMessageColor import MarqueeMessageColor
from models.MarqueeMessageFont import MarqueeMessageFont
from models.MarqueeMessageMode import MarqueeMessageMode


class TestMarqueeMessage(unittest.TestCase):
    
    def test_init(self):
        message = MarqueeMessage()
        self.assertEqual(message.text, "")
        self.assertEqual(message.color.name, MarqueeMessageColor.AUTOCOLOR.name)
        self.assertEqual(message.font.name, MarqueeMessageFont.SEVEN_HIGH_FANCY.name)
        self.assertEqual(message.mode.name, MarqueeMessageMode.ROLL_LEFT.name)

    def test_repr(self):
        message = MarqueeMessage("Hello", MarqueeMessageColor.RED, MarqueeMessageFont.SEVEN_HIGH_STD, MarqueeMessageMode.ROLL_RIGHT)
        self.assertEqual(repr(message), '{"text": "Hello", "color": "RED", "font": "SEVEN_HIGH_STD", "mode": "ROLL_RIGHT"}')

    def test_getMarqueeMessage(self):
        message = MarqueeMessage("Hello", MarqueeMessageColor.RED, MarqueeMessageFont.SEVEN_HIGH_STD, MarqueeMessageMode.ROLL_RIGHT)
        self.assertEqual(message.get_marquee_message(), {
            "text": "Hello",
            "color": "RED",
            "font": "SEVEN_HIGH_STD",
            "mode": "ROLL_RIGHT"
        })
    
    def test_setMarqueeMessage(self):
        message = MarqueeMessage()
        message.set_marquee_message("Hello", MarqueeMessageColor.RED, MarqueeMessageFont.SEVEN_HIGH_STD, MarqueeMessageMode.ROLL_RIGHT)
        self.assertEqual(message.text, "Hello")
        self.assertEqual(message.color.name, MarqueeMessageColor.RED.name)
        self.assertEqual(message.font.name, MarqueeMessageFont.SEVEN_HIGH_STD.name)
        self.assertEqual(message.mode.name, MarqueeMessageMode.ROLL_RIGHT.name)
    
    def test_createMarqueeMessageFromArtistAndSongTitle(self):
        message = MarqueeMessage()
        artist = "Artist"
        songTitle = "Song Title"
        expectedString = TestData.createArtistAndTitleString(artist, songTitle)
        result = message.create_marquee_message_from_artist_and_song_title(artist, songTitle)
        self.assertEqual(result, {
            "text": expectedString,
            "color": "AUTOCOLOR",
            "font": "SEVEN_HIGH_FANCY",
            "mode": "ROLL_LEFT"
        })
    
    def test_convertArtistTitleToMarqueeMessage(self):
        message = MarqueeMessage()
        artist = "Artist"
        songTitle = "Song Title"
        expectedString = TestData.createArtistAndTitleString(artist, songTitle)
        result = message.convert_artist_title_to_marquee_message(artist, songTitle)
        self.assertEqual(result, expectedString)
    
    def test_convertArtistTitleToMarqueeMessageLong(self):
        message = MarqueeMessage()
        artist = "A" * 100
        songTitle = "B" * 100
        expectedString = TestData.createArtistAndTitleString(artist, songTitle)
        result = message.convert_artist_title_to_marquee_message(artist, songTitle)
        self.assertEqual(result, expectedString)
    
    def test_convertArtistTitleToMarqueeMessageEmpty(self):
        message = MarqueeMessage()
        expectedString = TestData.createArtistAndTitleString("", "")
        result = message.convert_artist_title_to_marquee_message("", "")
        self.assertEqual(result, expectedString)
    
    def test_convertArtistTitleToMarqueeMessageSpecialChars(self):
        specialChars = "!@#$%^&*()"
        expectedString = TestData.createArtistAndTitleString(specialChars, specialChars)
        message = MarqueeMessage()
        result = message.convert_artist_title_to_marquee_message(specialChars, specialChars)
        self.assertEqual(result, expectedString)

    def test_extractArtistTitle(self):
        message = MarqueeMessage()
        artist = "Artist"
        songTitle = "Song Title"
        testString = TestData.createArtistAndTitleString(artist, songTitle)
        message.set_marquee_message(testString, MarqueeMessageColor.RED, MarqueeMessageFont.SEVEN_HIGH_STD, MarqueeMessageMode.ROLL_RIGHT)
        result = message.extract_artist_and_song_title_from_marquee_message()
        self.assertEqual(result, (artist, songTitle))
