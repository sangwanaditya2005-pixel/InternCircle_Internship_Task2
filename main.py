
def calculator():
    while True:
        print("\n--- Basic Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", a / b)

        except ValueError:
            print("Invalid input. Please enter numbers.")


def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid choice. Try again.")
            continue

        try:
            value = float(input("Enter value to convert: "))

            if choice == "1":
                print("Miles:", value * 0.621371)
            elif choice == "2":
                print("Fahrenheit:", (value * 9 / 5) + 32)

        except ValueError:
            print("Invalid input. Please enter a number.")


while True:
    print("\n=== InternCircle Calculator & Converter ===")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        unit_converter()
    elif choice == "3":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Try again.")
