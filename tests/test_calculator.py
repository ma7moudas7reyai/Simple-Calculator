import unittest

from SimpleCalc import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_division(self):
        self.assertEqual(calculate(10, 4, "/"), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(1, 0, "/")

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "^")


if __name__ == "__main__":
    unittest.main()
