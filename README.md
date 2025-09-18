# 🔑 Password Generator (Gen 2.0)

A simple yet effective password generator built with Python in Visual Studio Code.  
This project creates strong, random passwords to help users improve their online security.  

---

## 📖 Overview
This password generator prompts the user for the number of characters they want in their password and generates a random, secure password.  

- Written in **Python**  
- User chooses password length  
- Uses Python’s built-in `random` library  
- Produces **randomized characters** including letters, digits, and special characters  

---

## 🛠️ How It Works
1. The program asks the user:  
   ```
   How many characters do you want in your password?
   ```
2. The user enters a number (e.g., `12`).  
3. The program generates a password of that length using a **random mix of letters, numbers, and symbols**.  
4. The final password is displayed on the screen.  

---

## 💻 Code
```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator (Gen 2.0)!")
    try:
        length = int(input("How many characters do you want in your password? "))
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
        else:
            print("Your generated password is:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
```

---

## 🎯 Example Run
```
Welcome to the Password Generator (Gen 2.0)!
How many characters do you want in your password? 12
Your generated password is: a8@Lm#Qz9!Tk
```

---

## ⚡ Challenge (Gen 2.0 Exclusive)
Currently, the password generator creates **randomized** passwords of a user-defined length.  

👉 Challenge yourself to:
- Add an option where the user can **choose what types of characters** to include (letters, digits, symbols).  
- Example: Generate a password with only letters and numbers, no special characters.  

---

## ✅ Solution to Challenge
Here’s one way to solve it:  

```python
import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator (Gen 2.0 with Options)!")
    try:
        length = int(input("How many characters do you want in your password? "))
        
        use_letters = input("Include letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        if length < 4:
            print("Password length should be at least 4 characters for better security.")
        else:
            print("Your generated password is:", generate_password(length, use_letters, use_digits, use_symbols))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
```

---

## 📌 Key Takeaways
- Learned how to use **Python’s `random` and `string` libraries**.  
- Practiced **functions, input handling, and error checking**.  
- Implemented an optional **challenge** to give the generator more flexibility.  

---

## 🚀 Future Improvements
- Add a **GUI version** with Tkinter or PyQt.  
- Store generated passwords securely.  
- Add strength evaluation (weak, medium, strong).  

---

👨‍💻 Created with Python in **Visual Studio Code**
