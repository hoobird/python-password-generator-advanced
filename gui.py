import tkinter as tk
from generate_password import gui_generate_password

def onButtonClick():
    website = websiteEntry.get()
    login_id = loginidEntry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_specialcharacters = specialchars_var.get()
    include_numbers = numbers_var.get()
    passwordLength = lengthEntry.get()
    gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_specialcharacters, include_numbers, passwordLength)

# Tk window
window = tk.Tk()
window.title("Password Generator")

# website entry
tk.Label(window, text="Website:").pack()
websiteEntry = tk.Entry(window)
websiteEntry.pack(padx=20)

# login entry
tk.Label(window, text="Login ID:").pack(padx=20)
loginidEntry = tk.Entry(window)
loginidEntry.pack(padx=20)

# boolean checkboxes
numbers_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Numbers", variable=numbers_var).pack(padx=20)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var).pack(padx=20)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var).pack(padx=20)

specialchars_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Special Characters", variable=specialchars_var).pack(padx=20)

# Password Length entry
tk.Label(window, text="Password Length:").pack(padx=20)
lengthEntry = tk.Entry(window)
lengthEntry.pack(padx=20)

# # Password Length slider
# tk.Label(window, text="Password Length:").pack(padx=20)
# lengthSlider = tk.Scale(window, from_=8, to=32, orient=tk.HORIZONTAL)
# lengthSlider.pack(padx=20)
# window.mainloop()

# Generate Password button
generateButton = tk.Button(window, text="Generate Password", command=onButtonClick)
generateButton.pack()

# Mainloop
window.mainloop()