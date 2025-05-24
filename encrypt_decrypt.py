import os
import base64
import sys
import hashlib
import json
import tkinter as tk


def write_to_file():
    user_input = input("Do you want to write to a file? (yes/no): ").strip().lower()
    if user_input == 'yes':
        user_input = entry.get()
        with open("encryption.txt", 'a') as file:
            file.write(user_input + "\n")
        label.config(text="Data written to encryption.txt")
        print(f"Data written to {"encryption.txt"}")
    else:
        print("Data not written to file.")

def clear_text():
    entry.delete(0, tk.END)
    label.config(text="Enter your text:")

#create window
window = tk.Tk()
window.title("Encrypt/Decrypt Tool")
window.geometry("400x300")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

#button to submit input
button = tk.Button(window, text="Save", command=write_to_file)
button.pack(pady=5)

#add labels and text boxes
label = tk.Label(window, text="Enter the text you wanna encrypt:")
label.pack(pady=10)

window.mainloop()