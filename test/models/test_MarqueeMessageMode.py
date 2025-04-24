import unittest

from models.MarqueeMessageMode import MarqueeMessageMode


class Test_MarqueeMessageMode(unittest.TestCase):
    def test_marqueeMessageModeRotate(self):
        self.assertEqual("ROTATE", MarqueeMessageMode.ROTATE.name)

    def test_marqueeMessageModeHold(self):
        self.assertEqual("HOLD", MarqueeMessageMode.HOLD.name)

    def test_marqueeMessageModeRollUp(self):
        self.assertEqual("ROLL_UP", MarqueeMessageMode.ROLL_UP.name)

    def test_marqueeMessageModeRollDown(self):
        self.assertEqual("ROLL_DOWN", MarqueeMessageMode.ROLL_DOWN.name)

    def test_marqueeMessageModeRollLeft(self):
        self.assertEqual("ROLL_LEFT", MarqueeMessageMode.ROLL_LEFT.name)

    def test_marqueeMessageModeRollRight(self):
        self.assertEqual("ROLL_RIGHT", MarqueeMessageMode.ROLL_RIGHT.name)

    def test_marqueeMessageModeWipeUp(self):
        self.assertEqual("WIPE_UP", MarqueeMessageMode.WIPE_UP.name)

    def test_marqueeMessageModeWipeDown(self):
        self.assertEqual("WIPE_DOWN", MarqueeMessageMode.WIPE_DOWN.name)

    def test_marqueeMessageModeWipeLeft(self):
        self.assertEqual("WIPE_LEFT", MarqueeMessageMode.WIPE_LEFT.name)

    def test_marqueeMessageModeWipeRight(self):
        self.assertEqual("WIPE_RIGHT", MarqueeMessageMode.WIPE_RIGHT.name)

    def test_marqueeMessageModeScroll(self):
        self.assertEqual("SCROLL", MarqueeMessageMode.SCROLL.name)

    def test_marqueeMessageModeRollIn(self):
        self.assertEqual("ROLL_IN", MarqueeMessageMode.ROLL_IN.name)

    def test_marqueeMessageModeRollOut(self):
        self.assertEqual("ROLL_OUT", MarqueeMessageMode.ROLL_OUT.name)

    def test_marqueeMessageModeWipeIn(self):
        self.assertEqual("WIPE_IN", MarqueeMessageMode.WIPE_IN.name)

    def test_marqueeMessageModeWipeOut(self):
        self.assertEqual("WIPE_OUT", MarqueeMessageMode.WIPE_OUT.name)

    def test_marqueeMessageModeTwinkle(self):
        self.assertEqual("TWINKLE", MarqueeMessageMode.TWINKLE.name)

    def test_marqueeMessageModeSnow(self):
        self.assertEqual("SNOW", MarqueeMessageMode.SNOW.name)

    def test_marqueeMessageModeInterlock(self):
        self.assertEqual("INTERLOCK", MarqueeMessageMode.INTERLOCK.name)

    def test_marqueeMessageModeSwitch(self):
        self.assertEqual("SWITCH", MarqueeMessageMode.SWITCH.name)

    def test_marqueeMessageModeSpray(self):
        self.assertEqual("SPRAY", MarqueeMessageMode.SPRAY.name)

    def test_marqueeMessageModeStarburst(self):
        self.assertEqual("STARBURST", MarqueeMessageMode.STARBURST.name)

    def test_marqueeMessageModeWelcome(self):
        self.assertEqual("WELCOME", MarqueeMessageMode.WELCOME.name)

    def test_marqueeMessageModeSlotMachine(self):
        self.assertEqual("SLOT_MACHINE", MarqueeMessageMode.SLOT_MACHINE.name)
        
    def test_marqueeMessageModeThankYou(self):
        self.assertEqual("THANK_YOU", MarqueeMessageMode.THANK_YOU.name)

    def test_marqueeMessageModeNoSmoking(self):
        self.assertEqual("NO_SMOKING", MarqueeMessageMode.NO_SMOKING.name)

    def test_marqueeMessageModeDontDrinkDrive(self):
        self.assertEqual("DONT_DRINK_DRIVE", MarqueeMessageMode.DONT_DRINK_DRIVE.name)

    def test_marqueeMessageModeRunningAnimal(self):
        self.assertEqual("RUNNING_ANIMAL", MarqueeMessageMode.RUNNING_ANIMAL.name)

    def test_marqueeMessageModeFireworks(self):
        self.assertEqual("FIREWORKS", MarqueeMessageMode.FIREWORKS.name)

    def test_marqueeMessageModeTurboCar(self):
        self.assertEqual("TURBO_CAR", MarqueeMessageMode.TURBO_CAR.name)

    def test_marqueeMessageModeFlash(self):
        self.assertEqual("FLASH", MarqueeMessageMode.FLASH.name)

    def test_marqueeMessageModeAutoMode(self):
        self.assertEqual("AUTO_MODE", MarqueeMessageMode.AUTO_MODE.name)

    def test_marqueeMessageModeCompressedRotate(self):
        self.assertEqual("COMPRESSED_ROTATE", MarqueeMessageMode.COMPRESSED_ROTATE.name)

    def test_marqueeMessageModeExplode(self):
        self.assertEqual("EXPLODE", MarqueeMessageMode.EXPLODE.name)

    def test_marqueeMessageModeClock(self):
        self.assertEqual("CLOCK", MarqueeMessageMode.CLOCK.name)

    def test_marqueeMessageModeNewsFlash(self):
        self.assertEqual("NEWS_FLASH", MarqueeMessageMode.NEWS_FLASH.name)

    def test_marqueeMessageModeTrumpetAnimation(self):
        self.assertEqual("TRUMPET_ANIMATION", MarqueeMessageMode.TRUMPET_ANIMATION.name)

    def test_marqueeMessageModeFishAnimation(self):
        self.assertEqual("FISH_ANIMATION", MarqueeMessageMode.FISH_ANIMATION.name)

    def test_marqueeMessageModeBalloonAnimation(self):
        self.assertEqual("BALLOON_ANIMATION", MarqueeMessageMode.BALLOON_ANIMATION.name)

    def test_marqueeMessageModeCherryBomb(self):
        self.assertEqual("CHERRY_BOMB", MarqueeMessageMode.CHERRY_BOMB.name)

if __name__ == "__main__":
    unittest.main()