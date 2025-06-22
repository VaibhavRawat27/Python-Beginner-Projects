import random

def get_random_quote():
    quotes = [
        "Believe in yourself and all that you are.",
        "Dream big. Start small. Act now.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The best way to get started is to quit talking and begin doing.",
        "Do one thing every day that scares you.",
        "Hardships often prepare ordinary people for an extraordinary destiny."
    ]

    return random.choice(quotes)

if __name__ == "__main__":
    print("Your Quote of the Moment")
    print(get_random_quote())
