def perform_operation(num1, num2, operation):
    # Addition
    if operation == "add":
        return num1 + num2

    # Subtraction
    elif operation == "subtract":
        return num1 - num2

    # Multiplication
    elif operation == "multiply":
        return num1 * num2

    # Division
    elif operation == "divide":
        if num2 == 0:
            return "division by zero"
        return num1 / num2

    # Invalid operation
    else:
        return "invalid operation"
