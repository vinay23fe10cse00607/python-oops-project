import random
import string

class PasswordGenerator:
    def __init__(self):
        self.saved_passwords = {}

    def generate_password(self, length, use_uppercase=True, use_numbers=True, use_special_chars=True): 
        if length < 4:  
            raise ValueError("Password length must be at least 4.")

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        password = []
        if use_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_numbers:
            password.append(random.choice(string.digits))
        if use_special_chars:
            password.append(random.choice(string.punctuation))
        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)
        return ''.join(password)

    def save_password(self, name, password):
        self.saved_passwords[name] = password
        print(f"Password for '{name}' saved successfully.")

    def get_saved_password(self, name):
        return self.saved_passwords.get(name, "No password found for this name.")

def main():
    print("Welcome to the Random Password Generator!")
    generator = PasswordGenerator()

    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Retrieve Saved Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                length = int(input("Enter the length of the password: "))
                use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
                use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
                use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

                password = generator.generate_password(length, use_uppercase, use_numbers, use_special_chars)
                print(f"Generated Password: {password}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            name = input("Enter a name for the password: ")
            password = input("Enter the password to save: ")
            generator.save_password(name, password)

        elif choice == '3':
            name = input("Enter the name of the saved password: ")
            saved_password = generator.get_saved_password(name)
            print(f"Retrieved Password: {saved_password}")

        elif choice == '4':
            print("Thank you for using the Password Generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
