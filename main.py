from customtkinter import *
from PIL import Image
import tkinter as tk
import sqlite3
import webbrowser
import login

root = CTk()
root.state('zoomed')
root.title("Instructor ASAP")

logoin = CTkImage(dark_image=Image.open("D:\Project Examasap\INSTRUCTOR\Instrucor-Interface\main.png"), size=(1920, 1080))
logoin_right1 = CTkLabel(root, image=logoin, text="", fg_color="#333D79")
logoin_right1.place(relx=0.5, rely=0.5, anchor="center")

frame = CTkFrame(root, width=550, height=850, fg_color="black", corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center")


description = CTkLabel(frame, text=("Unlock student potential with our intuitive instructor app,\ndesigned to simplify teaching and amplify learning"),
                       font=("Segoe UI", 16), text_color="white")
description.place(relx=0.5, rely=0.2, anchor="center")

username_label = CTkLabel(frame, text="Username:", font=("Segoe UI", 16, "bold"), text_color="white")
username_label.place(relx=0.1, rely=0.4, anchor="w")

username_entry = CTkEntry(frame, width=350, height=40, corner_radius=10, placeholder_text="Enter your username", font=("Segoe UI", 16),text_color= "white")
username_entry.place(relx=0.1, rely=0.45, anchor="w")

password_label = CTkLabel(frame, text="Password:", font=("Segoe UI", 16, "bold"), text_color="#87CEEB")
password_label.place(relx=0.1, rely=0.55, anchor="w")

password_entry = CTkEntry(frame, width=350, height=40, corner_radius=10, placeholder_text="Enter your password", show="*", font=("Segoe UI", 16),text_color= "white")
password_entry.place(relx=0.1, rely=0.6, anchor="w")

show_password_var = tk.IntVar()
show_password_checkbox = CTkCheckBox(frame, text="Show Password", variable=show_password_var, command=lambda: show_password(password_entry, show_password_var),text_color_disabled= "None")
show_password_checkbox.place(relx=0.7, rely=0.6, anchor="e")

def show_password(entry, var):
    if var.get():
        entry.configure(show="")
    else:
        entry.configure(show="*")

def animate_frame():
    for i in range(50):
        frame.place(relx=0.2, rely=1.5 - i / 50, anchor="center")
        root.update()
        root.after(10)

animate_frame()

def initialize_db():
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(fullname, email, username, password):
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (fullname, email, username, password) VALUES (?, ?, ?, ?)', (fullname, email, username, password))
    conn.commit()
    conn.close()

def check_username(username):
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def open_register_window():
    register_window = CTkToplevel(root)
    register_window.title("Register")
    register_window.geometry("400x400")

    CTkLabel(register_window, text="Full Name:", font=("Segoe UI", 16)).place(relx=0.1, rely=0.1, anchor="w")
    fullname_entry = CTkEntry(register_window, width=300, height=30, corner_radius=10, font=("Segoe UI", 16))
    fullname_entry.place(relx=0.1, rely=0.15, anchor="w")

    CTkLabel(register_window, text="Email:", font=("Segoe UI", 16)).place(relx=0.1, rely=0.25, anchor="w")
    email_entry = CTkEntry(register_window, width=300, height=30, corner_radius=10, font=("Segoe UI", 16))
    email_entry.place(relx=0.1, rely=0.3, anchor="w")

    CTkLabel(register_window, text="Username:", font=("Segoe UI", 16)).place(relx=0.1, rely=0.4, anchor="w")
    username_entry = CTkEntry(register_window, width=300, height=30, corner_radius=10, font=("Segoe UI", 16))
    username_entry.place(relx=0.1, rely=0.45, anchor="w")

    CTkLabel(register_window, text="Password:", font=("Segoe UI", 16)).place(relx=0.1, rely=0.55, anchor="w")
    password_entry = CTkEntry(register_window, width=300, height=30, corner_radius=10, show="*", font=("Segoe UI", 16))
    password_entry.place(relx=0.1, rely=0.6, anchor="w")

    def register():
        fullname = fullname_entry.get()
        email = email_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        
        if fullname and email and username and password:
            if check_username(username):
                tk.messagebox.showwarning("Registration Error", "Username already exists. Please choose another.")
            else:
                register_user(fullname, email, username, password)
                tk.messagebox.showinfo("Success", "User registered successfully. Please login.")
                register_window.destroy()
        else:
            tk.messagebox.showwarning("Input Error", "All fields are required.")

    CTkButton(register_window, text="Register", command=register, width=150, height=40, corner_radius=10).place(relx=0.5, rely=0.8, anchor="center")

def contact_us():
    webbrowser.open("https://www.instagram.com/_dikshanta/")

def call_login():
    username = username_entry.get()
    password = password_entry.get()
    login.login(root, username, password, frame)

register_button = CTkButton(frame, text="Register", width=100, height=30, corner_radius=10, command=open_register_window)
register_button.place(relx=0.1, rely=0.7, anchor="w")

login_button = CTkButton(frame, text="Login", width=100, height=30, corner_radius=10, command=call_login)
login_button.place(relx=0.3, rely=0.7, anchor="w")

contact_button = CTkButton(frame, text="Contact Us", width=100, height=30, corner_radius=10, command=contact_us)
contact_button.place(relx=0.5, rely=0.7, anchor="w")

initialize_db()
root.mainloop()
