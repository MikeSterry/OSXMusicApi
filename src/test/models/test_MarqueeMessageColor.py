import unittest

from src.models.MarqueeMessageColor import MarqueeMessageColor


class Test_MarqueeMessageColor(unittest.TestCase):
    
    def test_marqueeMessageColorRed(self):
        self.assertEqual("RED", MarqueeMessageColor.RED.name)

    def test_marqueeMessageColorGreen(self):
        self.assertEqual("GREEN", MarqueeMessageColor.GREEN.name)

    def test_marqueeMessageColorAmber(self):
        self.assertEqual("AMBER", MarqueeMessageColor.AMBER.name)

    def test_marqueeMessageColorColorMix(self):
        self.assertEqual("COLOR_MIX", MarqueeMessageColor.COLOR_MIX.name)

    def test_marqueeMessageColorRainbow1(self):
        self.assertEqual("RAINBOW_1", MarqueeMessageColor.RAINBOW_1.name)

    def test_marqueeMessageColorRainbow2(self):
        self.assertEqual("RAINBOW_2", MarqueeMessageColor.RAINBOW_2.name)