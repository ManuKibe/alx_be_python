# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator # Import the SimpleCalculator class

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering addition,
    subtraction, multiplication, and division operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5)         # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)        # Negative and positive, sums to zero
        self.assertEqual(self.calc.add(-5, -3), -8)      # Negative numbers
        self.assertEqual(self.calc.add(0, 7), 7)         # Adding zero
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)   # Float numbers
        self.assertEqual(self.calc.add(100, 0), 100)     # Zero with positive

    def test_subtract(self):
        """
        Test the subtract method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.subtract(5, 2), 3)        # Positive result
        self.assertEqual(self.calc.subtract(2, 5), -3)       # Negative result
        self.assertEqual(self.calc.subtract(-1, 1), -2)      # Negative from negative
        self.assertEqual(self.calc.subtract(1, -1), 2)       # Subtracting a negative
        self.assertEqual(self.calc.subtract(0, 5), -5)       # Subtracting from zero
        self.assertEqual(self.calc.subtract(5, 0), 5)        # Subtracting zero
        self.assertEqual(self.calc.subtract(10.5, 5.5), 5.0) # Float numbers

    def test_multiply(self):
        """
        Test the multiply method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)        # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)      # Negative by positive
        self.assertEqual(self.calc.multiply(2, -3), -6)      # Positive by negative
        self.assertEqual(self.calc.multiply(-2, -3), 6)      # Negative by negative
        self.assertEqual(self.calc.multiply(0, 5), 0)        # Multiply by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)        # Zero by positive
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)    # Float numbers

    def test_divide(self):
        """
        Test the divide method, including normal division and division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)       # Normal division
        self.assertEqual(self.calc.divide(1, 2), 0.5)        # Float result
        self.assertEqual(self.calc.divide(-10, 2), -5.0)     # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5.0)     # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5.0)     # Both negative
        self.assertEqual(self.calc.divide(0, 5), 0.0)        # Zero numerator
        self.assertIsNone(self.calc.divide(10, 0))           # Division by zero should return None
        self.assertIsNone(self.calc.divide(0, 0))            # Division by zero (0/0) should also return None

if __name__ == '__main__':
    unittest.main() # This line allows running tests directly from the script
