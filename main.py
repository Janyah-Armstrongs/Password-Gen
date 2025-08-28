import random
import string

 Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

print("\n--- Password Generator ---")
length = int(input("Enter password length: "))
password = generate_password(length)
print(f"Your new password is: {password}")
