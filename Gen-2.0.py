import random
import string

def generate_password(base_word, birth_year, favorite_symbol, length=12):
    # Build the base part
    base = base_word.capitalize() + str(birth_year) + favorite_symbol
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # If base is too long, trim it but leave space for at least 2 random characters
    if len(base) >= length:
        trimmed_base = base[:length-2]  # keep most of the base
        random_part = "".join(random.choice(characters) for _ in range(2))  # always randomize
        return trimmed_base + random_part
    
    # Otherwise, fill in the rest with randomness
    random_part = "".join(random.choice(characters) for _ in range(length - len(base)))
    return base + random_part


# --- User Interaction ---
print("\n--- Personalized Password Generator (Gen 2.0) ---")

# Ask the user for input
base_word = input("What is a word you like (e.g., hobby, nickname)? ")
birth_year = input("What year were you born? ")
favorite_symbol = input("Pick your favorite symbol (e.g., @, #, $, %): ")
length = int(input("Enter desired total password length: "))

# Generate password
password = generate_password(base_word, birth_year, favorite_symbol, length)

# Display result
print(f"\nYour new password is: {password}")
