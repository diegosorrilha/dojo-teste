import unittest
from happy_numbers import happy_numbers

class TestHappyNumbers(unittest.TestCase):

    def test_happy_numbers(self):
        self.assertEqual(happy_numbers(), None)

unittest.main()
        
