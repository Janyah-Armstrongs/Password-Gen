# 🔑 Password Generator (Gen 1.0 & Gen 2.0)

A simple yet effective password generator built with Python in Visual Studio Code.  
This project evolves from a **basic random generator (Gen 1.0)** to an **upgraded personalized version (Gen 2.0)**.  

---

## 📖 Overview
- **Gen 1.0**: Generates a password of random letters, digits, and symbols.  
- **Gen 2.0**: Adds personalization by combining user-provided words, numbers, and symbols with randomness.  
- Both versions strengthen your understanding of Python basics and problem-solving.  

---

## 🛠️ How It Works
1. The program asks the user how long they want their password to be.  
2. Based on the version:  
   - **Gen 1.0**: Generates a completely random password.  
   - **Gen 2.0**: Asks personal questions and combines them with randomness.  
3. Prints the generated password.  

---

## 💻 Code (Gen 1.0)
```python
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

print("\n--- Password Generator (Gen 1.0) ---")
length = int(input("Enter password length: "))
password = generate_password(length)
print(f"Your new password is: {password}")
```

---

## 🎯 Example Run (Gen 1.0)
```
--- Password Generator (Gen 1.0) ---
Enter password length: 10
Your new password is: aD3@h8!zQp
```

---

## 💻 Code (Gen 2.0)
```python
import random
import string

def generate_password(base_word, birth_year, favorite_symbol, length=12):
    base = base_word.capitalize() + str(birth_year) + favorite_symbol
    characters = string.ascii_letters + string.digits + string.punctuation

    # If base is too long, trim it but leave space for at least 2 random characters
    if len(base) >= length:
        trimmed_base = base[:length-2]  # keep most of the base
        random_part = "".join(random.choice(characters) for _ in range(2))  # ensure randomness
        return trimmed_base + random_part

    # Otherwise, fill in with random characters
    random_part = "".join(random.choice(characters) for _ in range(length - len(base)))
    return base + random_part

print("\n--- Password Generator (Gen 2.0) ---")
base_word = input("What is a word you like (e.g., hobby, nickname)? ")
birth_year = input("What year were you born? ")
favorite_symbol = input("Pick your favorite symbol (e.g., @, #, $, %): ")
length = int(input("Enter desired total password length: "))

password = generate_password(base_word, birth_year, favorite_symbol, length)
print(f"\nYour new password is: {password}")
```

---

## 🎯 Example Run (Gen 2.0)
```
--- Password Generator (Gen 2.0) ---
What is a word you like (e.g., hobby, nickname)? gamer
What year were you born? 2002
Pick your favorite symbol (e.g., @, #, $, %): @
Enter desired total password length: 14

Your new password is: Gamer2002@!zP9
```

---

## ⚡ Challenge (Gen 2.0 Exclusive)
Problem:  
If the base word + year + symbol are longer than the password length you choose, the program will break.  

👉 Can you fix this?  

✅ Already solved in the code above by trimming the base and ensuring at least 2 random characters are always included.  

---

## 📌 Key Takeaways
- **Gen 1.0** taught basic randomization with `random` and `string`.  
- **Gen 2.0** added personalization, edge case handling, and more logic.  
- Practiced **functions, input handling, error prevention, and string manipulation**.  

---


👨‍💻 Created with Python in **Visual Studio Code**
