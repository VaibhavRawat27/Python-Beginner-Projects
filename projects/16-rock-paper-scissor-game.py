import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("\n=== Rock, Paper, Scissors Game ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye. 👋")
        break
