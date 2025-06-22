import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password should be at least 6 characters long.")
        return

    alphabets = string.ascii_letters  
    digits = string.digits           
    special = "!@#$%^&*()-_=+<>?/\\{}[]|"

    part_alpha = random.choices(alphabets, k=length//2)
    part_digit = random.choices(digits, k=length//4)
    part_special = random.choices(special, k=length - len(part_alpha) - len(part_digit))

    password_list = part_alpha + part_digit + part_special
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    print("Your Random Generated Password:", end=" ")
    print(generate_password(12))
