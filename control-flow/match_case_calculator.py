num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input(" Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1+num2
        print(f"the result is {result}")
    case "-":
        result = num1 -num2
        print(f"the result is {result}")
    case "*":
        result = num1 *num2
        print(f"the result is {result}")
    case "/":
        if num2 != 0:
            result = num1/num2
            print(f"the result is {result}")
        else:
            print("Error: cannot divide by zero.")
    case _:
        print("Invalid operation selected. please choose +, -, *, or /.")