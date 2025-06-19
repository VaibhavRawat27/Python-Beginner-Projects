def bill_splitter():
    print("💸 Welcome to the Bill Splitter App!")
    try:
        amount = float(input("Enter the total amount: ₹"))
        people_count = int(input("Enter the number of people to split the bill: "))
        
        if people_count <= 0:
            print("⚠️ Number of people must be at least 1.")
            return

        split_amount = round(amount / people_count, 2)
        
        print("\n--- Split Summary ---")
        print(f"Each person has to pay: ₹{split_amount}")
        print(f"Total collected: ₹{split_amount * people_count}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

bill_splitter()
