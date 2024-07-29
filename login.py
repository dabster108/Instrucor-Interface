import sqlite3
from customtkinter import CTkToplevel, CTkLabel, CTkImage, CTkButton, CTkEntry, CTkFrame
from PIL import Image
import tkinter as tk

def login_user(username, password):
    conn = sqlite3.connect('databaseexam.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def login(root, username, password, frame):
    for widget in frame.winfo_children():
        if isinstance(widget, CTkLabel) and widget != frame.children.get("welcome_label") and widget != frame.children.get("description"):
            widget.destroy()
    user = login_user(username, password)
    if user:
        print("Login successful")
        root.destroy()
        open_new_interface(user)
    else:
        error_label = CTkLabel(frame, text="Invalid username or password. Please try again.", font=("Segoe UI", 16, "bold"), text_color="red")
        error_label.place(relx=0.1, rely=0.75, anchor="w")

def open_new_interface(user):
    new_window = CTkToplevel()
    new_window.title("New Interface")
    new_window.state('zoomed')
    new_window.iconbitmap("D:\Project Examasap\open-book.ico")

    label = CTkLabel(new_window, text="Welcome to the new interface!", font=("Segoe UI", 16, "bold"))
    label.place(relx=0.5, rely=0.1, anchor="center")

    logoin = CTkImage(dark_image=Image.open("D:/Project Examasap/photo00.png"), size=(1920, 1080))
    logoin_right1 = CTkLabel(new_window, image=logoin, text="", fg_color="#333D79")
    logoin_right1.place(relx=0.5, rely=0.5, anchor="center")

    # Load and display the icon
    icon = CTkImage(dark_image=Image.open("D:\Project Examasap\open-book.ico"), size=(40, 40))  # Adjust size as needed
    icon_label = CTkLabel(new_window, image=icon, text="", fg_color="transparent")
    icon_label.place(relx=0.1, rely=0.1, anchor="center")  # Adjust position as needed

    # Create a frame for buttons at the top-right
    button_frame = CTkFrame(new_window, fg_color="transparent")
    button_frame.place(relx=0.9, rely=0.1, anchor="ne")

    # Function to change button color on hover
    def on_enter(button):
        button.configure(fg_color="#007BFF", text_color="white")  # Bright color on hover

    def on_leave(button):
        button.configure(fg_color="white", text_color="black")  # Default color

    # Functions to display different sections
    def show_description():
        clear_display_area()
        description_text = (
            "The Instructor App is a project developed by the talented students of AI Softwarica College. "
            "This innovative interface is designed to connect students with the college's most brilliant teachers, "
            "offering an interactive platform for personalized learning experiences.\n\n"
            "The app features a user-friendly interface built using Tkinter, where students can log in and manage their instructors. "
            "Students have the flexibility to add instructors of their choice, remove them as needed, or update instructor details, "
            "ensuring a dynamic and customized educational journey. The app supports full CRUD (Create, Read, Update, Delete) operations, "
            "making it a comprehensive tool for managing instructor-student interactions."
        )
        description_label = CTkLabel(new_window, text=description_text, font=("Segoe UI", 14))
        description_label.place(relx=0.5, rely=0.4, anchor="center")

    def show_contact():
        clear_display_area()
        contact_text = "Contact: 9843410777"
        contact_label = CTkLabel(new_window, text=contact_text, font=("Segoe UI", 14))
        contact_label.place(relx=0.5, rely=0.4, anchor="center")

    def show_profile():
        clear_display_area()
        profile_text = f"Username: {user[1]}\nEmail: {user[2]}"
        profile_label = CTkLabel(new_window, text=profile_text, font=("Segoe UI", 14))
        profile_label.place(relx=0.5, rely=0.4, anchor="center")

    def clear_display_area():
        for widget in new_window.winfo_children():
            if isinstance(widget, CTkLabel) and widget != logoin_right1 and widget != icon_label:
                widget.destroy()

    # Create buttons with hover effects
    description_button = CTkButton(
        button_frame, 
        text="Description", 
        width=120, 
        height=40, 
        command=show_description,
        corner_radius=10  # Rounded corners
    )
    description_button.pack(side='left', padx=5)  # Align buttons in a row with spacing
    description_button.bind("<Enter>", lambda e: on_enter(description_button))
    description_button.bind("<Leave>", lambda e: on_leave(description_button))

    contact_button = CTkButton(
        button_frame, 
        text="Contact", 
        width=120, 
        height=40, 
        command=show_contact,
        corner_radius=10
    )
    contact_button.pack(side='left', padx=5)
    contact_button.bind("<Enter>", lambda e: on_enter(contact_button))
    contact_button.bind("<Leave>", lambda e: on_leave(contact_button))

    profile_button = CTkButton(
        button_frame, 
        text="Profile", 
        width=120, 
        height=40, 
        command=show_profile,
        corner_radius=10
    )
    profile_button.pack(side='left', padx=5)
    profile_button.bind("<Enter>", lambda e: on_enter(profile_button))
    profile_button.bind("<Leave>", lambda e: on_leave(profile_button))

    # Add a line or box below the buttons
    line_frame = CTkFrame(new_window, width=400, height=2, fg_color="white")  # Thin white line
    line_frame.place(relx=0.9, rely=0.16, anchor="ne")  # Position below the buttons

    # Your existing database connection code (if needed)
    con = sqlite3.connect("databaseexam.db")
    cur = con.cursor()
    con.close()
