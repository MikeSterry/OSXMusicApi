import unittest
from test.utils.TestData import TestData

from models.MarqueeMessages import MarqueeMessages


class TestMarqueeMessages(unittest.TestCase):
    def setUp(self):
        self.marquee_messages = MarqueeMessages()

    def test_add_message(self):
        message = TestData.createMarqueeMessage("Test Message")
        self.marquee_messages.add_message(message)
        expected = [message]
        self.assertEqual(self.marquee_messages.get_messages(), expected)
        self.assertEqual(self.marquee_messages.get_messages()[0], message)
        self.assertEqual(len(self.marquee_messages.get_messages()), 1)

    def test_add_multiple_message(self):
        message1 = TestData.createMarqueeMessage("Test Message")
        message2 = TestData.createMarqueeMessage("Test Message2")
        message3 = TestData.createMarqueeMessage("Test Message3")
        self.marquee_messages.add_message(message1)
        self.marquee_messages.add_message(message2)
        self.marquee_messages.add_message(message3)
        expected = [message1, message2, message3]
        self.assertEqual(self.marquee_messages.get_messages(), expected)
        self.assertEqual(self.marquee_messages.get_messages()[1], message2)
        self.assertEqual(len(self.marquee_messages.get_messages()), 3)

    def test_get_body(self):
        message1 = TestData.createMarqueeMessage("Test Message")
        message2 = TestData.createMarqueeMessage("Test Message2")
        message3 = TestData.createMarqueeMessage("Test Message3")
        self.marquee_messages.add_message(message1)
        self.marquee_messages.add_message(message2)
        self.marquee_messages.add_message(message3)
        expected = {
            "messages": [message1, message2, message3]
        }
        self.assertEqual(self.marquee_messages.get_body(), expected)
    
# suite = unittest.TestLoader().loadTestsFromTestCase(TestMarqueeMessages)
# testResult = unittest.TextTestRunner(verbosity=2).run(suite)