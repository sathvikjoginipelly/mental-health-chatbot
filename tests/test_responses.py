import unittest
from chatbot.responses import get_response

class TestResponses(unittest.TestCase):
    def test_get_response(self):
        response = get_response("How are you?")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
