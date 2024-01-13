import string
import random
from tkinter import messagebox

def gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_specialcharacters, include_numbers, passwordLength):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_specialcharacters:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    try:
        passwordLength = int(passwordLength)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return
    
    password = "".join(random.choice(characters) for i in range(passwordLength))

    with open("passwords.txt", "a") as f:
        f.write(f"Website: {website}, Login: {login_id}, Password: {password}\n")
    
    messagebox.showinfo("Success", f"Password generated: {password}")