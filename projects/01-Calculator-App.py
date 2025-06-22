def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (**)")
        print("6. Modulus (%)")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                op = '+'
            elif choice == '2':
                result = num1 - num2
                op = '-'
            elif choice == '3':
                result = num1 * num2
                op = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2
                op = '/'
            elif choice == '5':
                result = num1 ** num2
                op = '**'
            elif choice == '6':
                result = num1 % num2
                op = '%'

            print(f"Result: {num1} {op} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculator()
