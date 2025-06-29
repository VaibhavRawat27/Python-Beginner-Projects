import random

def roll_dice():
    while True:
        num_dice = input("Roll how many dice? (1 or 2): ")
        if num_dice not in ['1', '2']:
            print("Please enter 1 or 2.")
            continue

        print("🎲 Rolling the dice...")
        if num_dice == '1':
            print(f"You got: {random.randint(1, 6)}")
        else:
            print(f"You got: {random.randint(1, 6)} and {random.randint(1, 6)}")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

roll_dice()
