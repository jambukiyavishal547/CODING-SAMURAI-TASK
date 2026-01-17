# Simple Calculator with Loop and Input Validation

while True:
    # Validate first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    # Validate second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    # Validate operator
    while True:
        choice = input("Enter operation (+, -, *, /): ")
        if choice in ['+', '-', '*', '/']:
            break
        else:
            print("❌ Invalid operation! Choose +, -, *, or /")

    # Perform calculation
    if choice == '+':
        print("Result:", num1 + num2)

    elif choice == '-':
        print("Result:", num1 - num2)

    elif choice == '*':
        print("Result:", num1 * num2)

    elif choice == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("❌ Error: Division by zero is not allowed")

    # Continue or exit
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("Calculator closed. Thank you!")
        break
