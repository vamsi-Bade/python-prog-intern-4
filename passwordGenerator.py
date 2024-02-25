import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Strong Password Generator!")
    print("========================================")
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            length = int(input("Enter the length of each password: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nGenerating Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()
