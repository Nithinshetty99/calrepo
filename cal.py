def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y


def calculator():
    print("Simple Command-Line Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        # Ask user to choose operation or quit
        operation = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")

        if operation == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid input. Please choose a valid operation.")
            continue

        try:
            # Take input for the two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the selected operation
        if operation == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")


# Run the calculator
calculator()
