def billing_system():
    products = {
        1: {"name": "Milk", "price": 32},
        2: {"name": "Butter", "price": 40},
        3: {"name": "Cottage Cheese", "price": 88},
        4: {"name": "Yogurt", "price": 30},
        5: {"name": "Butter Milk", "price": 25}
    }

    cart = []

    print("Welcome to Espero Dairy Mart Billing System!")

    while True:
        print("\nAvailable Products:")
        for key, item in products.items():
            print(f"{key}. {item['name']}: ₹{item['price']} per unit")

        try:
            choice = int(input("\nEnter product number to add to cart (or 0 to checkout): "))

            if choice == 0:
                break

            if choice not in products:
                print("Invalid product number. Please try again.")
                continue

            quantity = int(input(f"Enter quantity for {products[choice]['name']}: "))
            if quantity <= 0:
                print("Quantity must be at least 1.")
                continue

            cart.append({
                "name": products[choice]["name"],
                "price": products[choice]["price"],
                "quantity": quantity,
                "total": products[choice]["price"] * quantity
            })

            print(f"{quantity} x {products[choice]['name']} added to cart.")

        except ValueError:
            print("Please enter numeric input only.")

    if not cart:
        print("No items in cart. Exiting.")
        return

    print("\n--------- Cart Summary ---------")
    grand_total = 0
    for idx, item in enumerate(cart, 1):
        print(f"{idx}. {item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item['total']}")
        grand_total += item["total"]


    print(f"\nSubtotal: ₹{grand_total}")
    print(f"Total Amount to Pay: ₹{grand_total}")

    print("\nThank you for shopping at Espero Dairy Mart!")

billing_system()
