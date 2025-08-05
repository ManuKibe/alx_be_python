# class_static_methods_demo.py

class Calculator:
    """
    A simple Calculator class demonstrating the use of static methods and class methods.
    """

    # Class attribute: This attribute belongs to the class itself, not individual instances.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        Static methods do not receive a reference to the class (cls) or
        the instance (self). They are like regular functions but
        are logically grouped within the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        Class methods receive the class itself as the first argument (conventionally 'cls').
        This allows them to access and modify class-level attributes.
        """
        # Accessing the class attribute 'calculation_type' using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

