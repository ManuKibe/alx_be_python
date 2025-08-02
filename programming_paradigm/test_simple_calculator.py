2. Writing Unit Tests for a Simple Calculator Class
mandatory
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

Provided: simple_calculator.py
You’re given a SimpleCalculator class with basic arithmetic operations. Your task is to write unit tests to verify its correctness.

# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
Task: Write Unit Tests in test_simple_calculator.py
Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.

Guidelines for Writing Tests:
Import the Necessary Modules:

Import the unittest module and the SimpleCalculator class from simple_calculator.py.
Define a Test Class:

Create a test class that inherits from unittest.TestCase.
Write Test Methods:

Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
Include tests for edge cases, such as dividing by zero.
Use Assertions to Verify Results:

Utilize self.assertEqual() to check for expected outcomes.
For the divide method, ensure you test both normal operation and division by zero.
Running Your Tests:

Run your tests using the command line: python -m unittest test_simple_calculator.py.
Example Test Method Structure:
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
Note for you:
Your goal is to think like a tester and identify as many relevant test cases as possible for each method.
Pay special attention to potential edge cases, such as division by zero, which could lead to unexpected behaviors if not properly handled.
Writing comprehensive tests not only helps ensure your code is working correctly but also improves your understanding of how the code operates under different conditions.
Repo:

GitHub repository: alx_be_python
Directory: programming_paradigm
File: test_simple_calculator.py
