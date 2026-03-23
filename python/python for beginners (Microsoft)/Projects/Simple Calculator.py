# Continuous Simple Calculator

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /) or 'q' to quit: ")

    if operation == "q":
        print("Calculator closed. Goodbye!")
        break
    elif operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation"

    print("Result:", result)
    print("-" * 20)  # Separator for readability