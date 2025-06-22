def atm_software():
    balance = 10000  
    pin = 1234
    statement = []  

    print("\nLogin Successful!")
    
    while True:
        print("\n========= ATM MENU =========")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Money")
        print("5. Change PIN")
        print("6. Mini Statement")
        print("7. Exit")
        print("============================")
        
        choice = input("Enter operation (1-7): ")

        if choice == '1':
            print(f"Current Balance: ₹{balance}")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break


        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > balance:
                    print("Insufficient funds!")
                elif amount <= 0:
                    print("Enter a valid amount.")
                else:
                    balance -= amount
                    statement.append(f"Withdrawn: ₹{amount}")
                    print(f"₹{amount} withdrawn successfully.")
            except ValueError:
                print("Invalid input.")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break

        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Enter a valid amount.")
                else:
                    balance += amount
                    statement.append(f"Deposited: ₹{amount}")
                    print(f"₹{amount} deposited successfully.")
            except ValueError:
                print("Invalid input.")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break

        elif choice == '4':
            try:
                receiver = input("Enter recipient account number: ")
                amount = float(input("Enter amount to transfer: ₹"))
                if amount > balance:
                    print("Insufficient balance!")
                elif amount <= 0:
                    print("Enter a valid amount.")
                else:
                    balance -= amount
                    statement.append(f"Transferred ₹{amount} to {receiver}")
                    print(f"₹{amount} transferred to {receiver}.")
            except ValueError:
                print("Invalid input.")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break

        elif choice == '5':
            try:
                current_pin = int(input("Enter current PIN: "))
                if current_pin != pin:
                    print("Incorrect current PIN.")
                else:
                    new_pin = int(input("Enter new PIN: "))
                    confirm_pin = int(input("Confirm new PIN: "))
                    if new_pin == confirm_pin:
                        pin = new_pin
                        print("PIN changed successfully.")
                    else:
                        print("PINs do not match.")
            except ValueError:
                print("Invalid input.")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break

        elif choice == '6':
            print("Mini Statement:")
            if not statement:
                print("No transactions yet.")
            else:
                for entry in statement[-5:]:
                    print(f"- {entry}")

            x = int(input("Do you want to continue: Enter 1 for yes | Enter 0 for no: "))
            if x==1:
                break

        elif choice == '7':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Main execution
print("Welcome to the ATM!")
try:
    pin_input = int(input("Please enter your PIN to get started: "))
    if pin_input == 1234:
        atm_software()
    else:
        print("Invalid PIN! Please try again later.")
except ValueError:
    print("Invalid input! PIN must be numeric.")
