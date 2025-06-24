# Grocery Category Recommender
import random

categories = {
    "Fruits": ["Apples", "Bananas", "Oranges", "Grapes", "Mangoes"],
    "Vegetables": ["Tomatoes", "Potatoes", "Spinach", "Onions", "Carrots"],
    "Dairy": ["Milk", "Cheese", "Yogurt", "Butter", "Paneer"],
    "Snacks": ["Chips", "Biscuits", "Chocolate", "Popcorn", "Cookies"],
    "Beverages": ["Tea", "Coffee", "Juice", "Soda", "Milkshake"]
}

shopping_list = []

def recommend_items(category):
    if category in categories:
        suggestions = random.sample(categories[category], 3)
        print(f"Recommended items from {category}: {', '.join(suggestions)}")
    else:
        print("Invalid category.")

def view_list():
    if shopping_list:
        print("\n🛒 Your Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")

def main():
    while True:
        print("\n🛍️ Grocery Category Recommender")
        print("1. View Categories")
        print("2. Get Recommendations")
        print("3. Add Item to Shopping List")
        print("4. View Shopping List")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")
        if choice == '1':
            print("\nAvailable Categories:")
            for cat in categories:
                print(f"- {cat}")
        elif choice == '2':
            cat = input("Enter category: ").title()
            recommend_items(cat)
        elif choice == '3':
            item = input("Enter item to add: ").title()
            shopping_list.append(item)
            print(f"{item} added to your list.")
        elif choice == '4':
            view_list()
        elif choice == '5':
            print("Thank you for using Grocery Category Recommender!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
