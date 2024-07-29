from customtkinter import *
from PIL import Image
import tkinter as tk
import sqlite3
import webbrowser
import login

root = CTk()
root.state('zoomed')
root.title("Instructor ASAP")


logoin = CTkImage(dark_image=Image.open("D:/Project Examasap/photo3.jpg"), size=(1920, 1080))
logoin_right1 = CTkLabel(root, image=logoin, text="", fg_color="#333D79")
logoin_right1.place(relx=0.5, rely=0.5, anchor="center")

frame = CTkFrame(root, width=550, height=850, fg_color="gray20", corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center")


welcome_label = CTkLabel(frame, text="Welcome to Instructor App", font=("Wensley", 28, "bold"), text_color="white")
welcome_label.place(relx=0.5, rely=0.1, anchor="n")

description = CTkLabel(frame, text=("Unlock student potential with our intuitive instructor app,\ndesigned to simplify teaching and amplify learning"),
                       font=("Segoe UI", 16), text_color="white")
description.place(relx=0.5, rely=0.2, anchor="center")



username_label = CTkLabel(frame, text="Username:", font=("Segoe UI", 16, "bold"), text_color="yellow")
username_label.place(relx=0.1, rely=0.4, anchor="w")

username_entry = CTkEntry(frame, width=350, height=40, corner_radius=10, placeholder_text="Enter your username", font=("Segoe UI", 16))
username_entry.place(relx=0.1, rely=0.45, anchor="w")

password_label = CTkLabel(frame, text="Password:", font=("Segoe UI", 16, "bold"), text_color="#87CEEB")
password_label.place(relx=0.1, rely=0.55, anchor="w")

password_entry = CTkEntry(frame, width=350, height=40, corner_radius=10, placeholder_text="Enter your password", show="*", font=("Segoe UI", 16))
password_entry.place(relx=0.1, rely=0.6, anchor="w")

show_password_var = tk.IntVar()
show_password_checkbox = CTkCheckBox(frame, text="Show Password", variable=show_password_var, command=lambda: show_password(password_entry, show_password_var))
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
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def check_username(username):
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchall()
    conn.close()
    return user

def register():
    username = username_entry.get()
    password = password_entry.get()
    for widget in frame.winfo_children():
        if isinstance(widget, CTkLabel) and widget != welcome_label and widget != description:
            widget.destroy()
    if username and password:
        if check_username(username):
            error_label = CTkLabel(frame, text="Username already exists. Please login.", font=("Segoe UI", 16, "bold"), text_color="white")
            error_label.place(relx=0.1, rely=0.65, anchor="w")
        else:
            register_user(username, password)
            success_label = CTkLabel(frame, text="User registered successfully. Please login.", font=("Segoe UI", 16, "bold"), text_color="white")
            success_label.place(relx=0.1, rely=0.65, anchor="w")
    else:
        error_label = CTkLabel(frame, text="Please enter a username and password.", font=("Segoe UI", 16, "bold"), text_color="white")
        error_label.place(relx=0.1, rely=0.65, anchor="w")

def contact_us():
    webbrowser.open("https://www.instagram.com/_dikshanta/")

def call_login():
    username = username_entry.get()
    password = password_entry.get()
    login.login(root, username, password, frame)

register_button = CTkButton(frame, text="Register", width=100, height=30, corner_radius=10, command=register)
register_button.place(relx=0.1, rely=0.7, anchor="w")

login_button = CTkButton(frame, text="Login", width=100, height=30, corner_radius=10, command=call_login)
login_button.place(relx=0.3, rely=0.7, anchor="w")

contact_button = CTkButton(frame, text="Contact Us", width=100, height=30, corner_radius=10, command=contact_us)
contact_button.place(relx=0.5, rely=0.7, anchor="w")

initialize_db()
root.mainloop()


