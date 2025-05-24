import os
import base64
import sys
import hashlib
import json
import tkinter as tk


def show_text(text):
    user_input = entry.get()
    if user_input:
        text.delete(1.0, tk.END)  # Clear the text box
        text.insert(tk.END, user_input)  # Insert the user input

#create window
window = tk.Tk()
window.title("Encrypt/Decrypt Tool")
window.geometry("400x300")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

#button to submit input
button = tk.Button(window, text="Submit", command = show_text)
button2 = tk.Button(window, text="Clear", command=lambda: entry.delete(0, tk.END))
button.pack(pady=3)

#add labels and text boxes
label = tk.Label(window, text="Enter your text:")
label.pack(pady=10)

window.mainloop()