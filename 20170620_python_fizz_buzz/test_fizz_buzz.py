import unittest
from fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(), None)

unittest.main()
        
