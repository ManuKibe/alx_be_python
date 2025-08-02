# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_add(self):
        """
        Test the add method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(-1, -1), -2, "Should be -2")
        self.assertEqual(self.calc.add(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.add(100, 200), 300, "Should be 300")
        self.assertEqual(self.calc.add(5, 0), 5, "Should be 5")
        self.assertEqual(self.calc.add(0, 7), 7, "Should be 7")
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "Should handle floats")
        self.assertEqual(self.calc.add(-2.5, 2.5), 0.0, "Should handle negative floats")


    def test_subtract(self):
        """
        Test the subtract method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2, "Should be 2")
        self.assertEqual(self.calc.subtract(3, 5), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(1, -1), 2, "Should be 2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.subtract(10, 0), 10, "Should be 10")
        self.assertEqual(self.calc.subtract(0, 10), -10, "Should be -10")
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0, "Should handle floats")
        self.assertEqual(self.calc.subtract(-5.0, -2.0), -3.0, "Should handle negative floats")


    def test_multiply(self):
        """
        Test the multiply method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(-1, 5), -5, "Should be -5")
        self.assertEqual(self.calc.multiply(-1, -1), 1, "Should be 1")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(1, 10), 10, "Should be 10")
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0, "Should handle floats")
        self.assertEqual(self.calc.multiply(-3.0, 4.0), -12.0, "Should handle negative floats")


    def test_divide(self):
        """
        Test the divide method with various positive, negative, and zero inputs,
        including the crucial division by zero edge case.
        """
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Should be 2.0")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")
        self.assertEqual(self.calc.divide(-10, 2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(10, -2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(-10, -2), 5.0, "Should be 5.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "Should be 0.0")
        self.assertIsNone(self.calc.divide(5, 0), "Should return None for division by zero")
        self.assertIsNone(self.calc.divide(0, 0), "Should return None for 0 divided by 0")
        self.assertEqual(self.calc.divide(7.0, 2.0), 3.5, "Should handle floats")


if __name__ == '__main__':
    unittest.main()

