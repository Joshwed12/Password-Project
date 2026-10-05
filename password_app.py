import secrets
import string
import tkinter as tk
from tkinter import ttk 
from pathlib import Path

word_file = Path(__file__).parent / "words.txt"

words = [
    line.split()[1]
    for line in word_file.read_text(encoding="utf-8").splitlines()
    if line.strip()

]

symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
separators = string.digits + symbols

# Generate a password by randomly selecting multiple words from the list and concatenating them with random separators

def generate_password():
    # Randomly choose 3, 4, or 5 words.
    word_count = secrets.randbelow(3) + 3

    selected_words = [
        secrets.choice(words)
        for _ in range(word_count)
    ]

    # Place a random digit or symbol between words.
    password = selected_words[0]

    for word in selected_words[1]:
        password += secrets.choice(separators) + word

    # Guarantee a digit and a symbol at the end.
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)

    # Display the password in the app's text box.
    result.set(password)

def copy_password():
    if result.get():
        window.clipboard_clear()
        window.clipboard_append(result.get())
        status.set("Password copied to clipboard!")
    else:
        status.set("No password to copy.")


# Create the desktop window.
window = tk.Tk()
window.title("My Password Generator")
window.geometry("650x300")
# Store the text displayed in the password box.
result = tk.StringVar()
status = tk.StringVar()

title = ttk.Label(
    window,
    text="Random Passphrase Generator",
    font=("Arial", 18)
)
title.pack(pady=20)

password_box = ttk.Entry(
    window,
    textvariable=result,
    width=65,
    state="readonly"
)
password_box.pack(padx=20, fill="x")

generate_button = ttk.Button(
    window,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=(20, 5))

copy_button = ttk.Button(
    window,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=5)

status_label = ttk.Label(
    window,
    textvariable=status
)
status_label.pack(pady=10)

window.mainloop()   