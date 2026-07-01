import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import json

PASSWORD_LENGTH = 15

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            #Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found...")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="No password found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = ""
    for _ in range(PASSWORD_LENGTH):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("passwords.json", "w") as file:
                #Writing updated data to file
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)

logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = tk.Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, sticky="e")
email_label = tk.Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, sticky="e")
password_label = tk.Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "dkolomy@hotmail.com")
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
search_button = tk.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="ew")

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew")

add_button = tk.Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()