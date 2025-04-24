import unittest

from models.MarqueeMessageFont import MarqueeMessageFont


class Test_MarqueeMessageFont(unittest.TestCase):
    def test_marqueeMessageFontFiveHighStd(self):
        self.assertEqual("FIVE_HIGH_STD", MarqueeMessageFont.FIVE_HIGH_STD.name)

    def test_marqueeMessageFontSevenHighStd(self):
        self.assertEqual("SEVEN_HIGH_STD", MarqueeMessageFont.SEVEN_HIGH_STD.name)

    def test_marqueeMessageFontSevenHighFancy(self):
        self.assertEqual("SEVEN_HIGH_FANCY", MarqueeMessageFont.SEVEN_HIGH_FANCY.name)