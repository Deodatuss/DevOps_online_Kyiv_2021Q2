import unittest
import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_fizz(self):
        number = 6
        result = fizzbuzz.get_reply(number)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10
        result = fizzbuzz.get_reply(number)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        number = 15
        result = fizzbuzz.get_reply(number)
        self.assertEqual(result, 'FizzBuzz')

    def test_fizzbuzz_type(self):
        number = 15
        result = fizzbuzz.get_reply(number)
        self.assertEqual(type(result), type('str'))

    def test_failing_fizzbuzz_type(self):
        number = 15
        result = fizzbuzz.get_reply(number)
        self.assertNotEqual(type(result), type(3))


if __name__ == '__main__':
    unittest.main()
