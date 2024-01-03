import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."


def logarithm(x):
    return math.log10(x)


def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot calculate square root of a negative number."


def simple_calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Logarithmic values")
        print("6. Square root")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['5', '6']:
                num = float(input("Enter a number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = logarithm(num)
            elif choice == '6':
                result = square_root(num)

            print(f"Result: {result}")

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    simple_calculator()
