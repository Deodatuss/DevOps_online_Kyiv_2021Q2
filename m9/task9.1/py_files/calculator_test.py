import unittest
import calculator


class CalculatorTests(unittest.TestCase):
    def test_plus(self):
        number1 = 10
        number2 = 10
        oper = '+'
        result = calculator.calc(number1, number2, oper)
        self.assertEqual(result, 20)

    def test_minus(self):
        number1 = 6
        number2 = 10
        oper = '-'
        result = calculator.calc(number1, number2, oper)
        self.assertEqual(result, -4)

    def test_divide(self):
        number1 = 15
        number2 = 2
        oper = '/'
        result = calculator.calc(number1, number2, oper)
        self.assertEqual(result, 7.5)

    def test_power(self):
        number1 = 2
        number2 = 5
        oper = '^'
        result = calculator.calc(number1, number2, oper)
        self.assertEqual(result, 32)

    @unittest.expectedFailure
    def test_failing_number_type(self):
        number1 = [2]
        number2 = 5
        oper = '^'
        calculator.calc(number1, number2, oper)

    @unittest.expectedFailure
    def test_failing_operation(self):
        number1 = 2
        number2 = 5
        oper = '42'
        calculator.calc(number1, number2, oper)


if __name__ == '__main__':
    unittest.main()
