import random
import string

def generate_password(base_word, birth_year, favorite_symbol, length=12):
    # Start with user info
    base = base_word.capitalize() + str(birth_year)

    # Add some randomness
    characters = string.ascii_letters + string.digits + string.punctuation
    random_part = "".join(random.choice(characters) for _ in range(length - len(base) - 1))

    # Mix in their favorite symbol
    password = base + favorite_symbol + random_part
    return password

print("\n--- Unique Password Generator ---")

# Ask the user some questions
base_word = input("What is a word you like (e.g., hobby, nickname)? ")
birth_year = input("What year were you born? ")
favorite_symbol = input("Pick your favorite symbol (e.g., @, #, $, %): ")
length = int(input("Enter desired total password length: "))

# Generate password
password = generate_password(base_word, birth_year, favorite_symbol, length)
print(f"\nYour new password is: {password}")
