import unittest
from fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(), None)

    def teste_passando_1_retorna_2(self):
        self.assertEqual(fizz_buzz(1), 2)

unittest.main()
        
