import json
import requests
import os

# Load local dictionary or create empty
def load_local_dict():
    if os.path.exists("my_dict.json"):
        with open("my_dict.json", "r") as f:
            return json.load(f)
    return {}

# Save dictionary
def save_local_dict(dictionary):
    with open("my_dict.json", "w") as f:
        json.dump(dictionary, f, indent=2)

# Get definition from online API
def get_definition_online(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            meaning = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
            return meaning
        else:
            return None
    except:
        return None

# Main menu
def main():
    local_dict = load_local_dict()

    while True:
        print("\n📘 My Dictionary")
        print("1. Search word")
        print("2. Add custom word")
        print("3. View all saved words")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            word = input("Enter word to search: ").lower()
            if word in local_dict:
                print(f"\n🔍 {word} ➤ {local_dict[word]}")
            else:
                print("Searching online...")
                meaning = get_definition_online(word)
                if meaning:
                    print(f"\n🌐 {word} ➤ {meaning}")
                    save = input("Save this word to local dictionary? (y/n): ").lower()
                    if save == "y":
                        local_dict[word] = meaning
                        save_local_dict(local_dict)
                else:
                    print("❌ Word not found online.")
        
        elif choice == "2":
            word = input("Enter new word: ").lower()
            meaning = input("Enter meaning: ")
            local_dict[word] = meaning
            save_local_dict(local_dict)
            print("✅ Word added.")

        elif choice == "3":
            if local_dict:
                print("\n📚 Saved Words:")
                for word, meaning in local_dict.items():
                    print(f"• {word}: {meaning}")
            else:
                print("No words saved yet.")

        elif choice == "4":
            print("Goodbye! 📕")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
