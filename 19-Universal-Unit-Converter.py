def length_converter():
    km = float(input("Enter value in kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles:.2f} miles")

def weight_converter():
    kg = float(input("Enter value in kilograms: "))
    pounds = kg * 2.20462
    print(f"{kg} kg = {pounds:.2f} lbs")

def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

def currency_converter():
    inr = float(input("Enter amount in INR: "))
    usd = inr / 83.0  # Example conversion rate
    print(f"₹{inr} INR = ${usd:.2f} USD")

def main():
    while True:
        print("\n🧮 Universal Unit Converter")
        print("1. Length (km ⇄ miles)")
        print("2. Weight (kg ⇄ lbs)")
        print("3. Temperature (°C ⇄ °F)")
        print("4. Currency (INR ⇄ USD)")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")
        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            currency_converter()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
