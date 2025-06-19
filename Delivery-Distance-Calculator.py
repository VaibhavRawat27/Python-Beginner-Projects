def delivery_price_calculator():
    print("📦 Welcome to the Delivery Price Calculator!")
    
    try:
        item_price = float(input("Enter the item price (₹): "))
        distance_km = float(input("Enter delivery distance in kilometers: "))
        
        if item_price < 0 or distance_km < 0:
            print("⚠️ Amount and distance must be non-negative.")
            return
        
        delivery_charge = round(distance_km * 2, 2)  # ₹2 per km
        total_amount = round(item_price + delivery_charge, 2)
        
        print("\n--- Payment Summary ---")
        print(f"Item Price      : ₹{item_price}")
        print(f"Delivery Charge : ₹{delivery_charge} (₹2/km)")
        print(f"Total to Pay    : ₹{total_amount}")
    
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

delivery_price_calculator()
