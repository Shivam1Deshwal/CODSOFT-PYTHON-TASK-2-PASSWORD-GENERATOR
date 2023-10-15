import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits 

    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))

        if length < 1:
            print("Password length must be at least 1 character.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid password length (a positive integer).")

if __name__ == "__main__":
    main()
