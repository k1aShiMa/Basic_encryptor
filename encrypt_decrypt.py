import os
import base64
import sys
import hashlib
import json
import tkinter as tk


def write_to_file():
    user_input = entry.get()

    if len(user_input) < 6:
        label.config(text="Please enter a longer text (at least 6 characters).")
        return

    #encode the input
    hash_key = hashlib.sha512(user_input.encode()).hexdigest()

    with open("encryption.txt", 'a') as file:
        file.write(hash_key + "\n")
    label.config(text="Data written to encryption.txt")

# Function to clear the text box and reset the label
def clear_text():
    entry.delete(0, tk.END)
    label.config(text="Enter the text you wanna encrypt:")

# Function to exit the program
def exit_program():
    sys.exit()

# Function to check if the file exists and read its content
def read_file():
    if os.path.exists("encryption.txt"):
        with open("encryption.txt", 'r') as file:
            content = file.read()
        return content
    else:
        return "File does not exist."

#create window
window = tk.Tk()
window.title("Encrypt/Decrypt Tool")
window.geometry("400x300")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

#button to read the file
read_button = tk.Button(window, text="Read encryption.txt", command=lambda: label.config(text=read_file()))
read_button.pack(pady=10)

#button to encrypt into a file
save_button = tk.Button(window, text="Save sha512 hash", command=write_to_file)
save_button.pack(pady=5)

#button to clear the text box
clear_text_button = tk.Button(window, text="Clear Text", command=clear_text)
clear_text_button.pack(pady=5)

#exit button
exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack(pady=5)

#add labels and text boxes
label = tk.Label(window, text="Enter the text you wanna encrypt:")
label.pack(pady=10)

window.mainloop()