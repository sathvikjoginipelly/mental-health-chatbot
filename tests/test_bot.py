import unittest
from chatbot.bot import get_bot_response

class TestBot(unittest.TestCase):
    def test_get_bot_response(self):
        response = get_bot_response("Hello")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
