import random
import string

def generate_password(pass_length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password_combo = letters + digits + symbols
    password = random.sample(password_combo, length)

    return "".join(password)

def main():
    while True:
        try:
            pass_length = int(input("Enter the desired length of the password (must be 8 characters or more): "))
            if pass_length < 8:
                print("Password length must be 8 characters at least.")
                continue
            password = generate_password(pass_length)
            print("Generated password: ", password)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
