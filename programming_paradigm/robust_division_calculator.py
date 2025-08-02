# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str or float): The numerator for the division.
        denominator (str or float): The denominator for the division.

    Returns:
        str: An error message if an exception occurs, otherwise the result of the division
             formatted as a string.
    """
    try:
        # Attempt to convert inputs to float. This will raise ValueError if non-numeric.
        num = float(numerator)
        den = float(denominator)

        # Perform the division. This will raise ZeroDivisionError if denominator is 0.
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Catch and handle division by zero error
        return "Error: Cannot divide by zero."
    except ValueError:
        # Catch and handle non-numeric input error
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"

