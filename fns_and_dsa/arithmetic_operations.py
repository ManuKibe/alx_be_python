def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - float or str: Result of the operation or error message if division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Unsupported operation"

