import sqlite3
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkImage, CTkButton, CTkCheckBox, CTkFrame
from PIL import Image
import tkinter as tk

def login_user(username, password):
    try:
        conn = sqlite3.connect('databaseexam.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    except Exception as e:
        print(f"Error in login_user: {e}")
        return None

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

    label = CTkLabel(new_window, text="Welcome to the new interface!", font=("Segoe UI", 20, "bold"))
    label.place(relx=0.5, rely=0.1, anchor="center")

    try:
        logoin = CTkImage(dark_image=Image.open("D:\\Project Examasap\\Instrucor-Interface\\photo00.png"), size=(1920, 1080))
        logoin_right1 = CTkLabel(new_window, image=logoin, text="", fg_color="#333D79")
        logoin_right1.place(relx=0.5, rely=0.5, anchor="center")
    except Exception as e:
        print(f"Error loading background image: {e}")

    try:
        icon = CTkImage(dark_image=Image.open("D:\\Project Examasap\\Instrucor-Interface\\Book-open_icon-icons.com_52251.ico"), size=(40, 40))
        icon_label = CTkLabel(new_window, image=icon, text="", fg_color="transparent")
        icon_label.place(relx=0.05, rely=0.1, anchor="n")
    except Exception as e:
        print(f"Error loading icon image: {e}")

    button_frame = CTkFrame(new_window, fg_color="transparent")
    button_frame.place(relx=0.9, rely=0.1, anchor="ne")

    def show_tooltip(event, text, width, height):
        global tooltip
        tooltip = CTkLabel(new_window, text=text, font=("Segoe UI", 12), fg_color="black", text_color="white", width=width, height=height, corner_radius=10, wraplength=width - 20)
        tooltip.place(x=event.x_root + 10, y=event.y_root, anchor="nw")

    def hide_tooltip(event):
        global tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    def show_description_tooltip(event):
        text = ("The Instructor App is a project developed by the talented students of AI Softwarica College. "
                "This innovative interface is designed to connect students with the college's most brilliant teachers, "
                "offering an interactive platform for personalized learning experiences.\n\n"
                "The app features a user-friendly interface built using Tkinter, where students can log in and manage their instructors. "
                "Students have the flexibility to add instructors of their choice, remove them as needed, or update instructor details, "
                "ensuring a dynamic and customized educational journey. The app supports full CRUD (Create, Read, Update, Delete) operations, "
                "making it a comprehensive tool for managing instructor-student interactions.")
        show_tooltip(event, text, 500, 200)

    def show_contact_tooltip(event):
        text = "Contact: 9843410777"
        show_tooltip(event, text, 200, 50)

    def show_profile_tooltip(event):
        text = f"Username: {user[1]}\nEmail: {user[2]}"
        show_tooltip(event, text, 300, 100)

    description_button = CTkButton(button_frame, text="Description", width=120, height=40, corner_radius=10)
    description_button.pack(side='left', padx=5)
    description_button.bind("<Enter>", show_description_tooltip)
    description_button.bind("<Leave>", hide_tooltip)

    contact_button = CTkButton(button_frame, text="Contact", width=120, height=40, corner_radius=10)
    contact_button.pack(side='left', padx=5)
    contact_button.bind("<Enter>", show_contact_tooltip)
    contact_button.bind("<Leave>", hide_tooltip)

    profile_button = CTkButton(button_frame, text="Profile", width=120, height=40, corner_radius=10)
    profile_button.pack(side='left', padx=5)
    profile_button.bind("<Enter>", show_profile_tooltip)
    profile_button.bind("<Leave>", hide_tooltip)

    line_frame = CTkFrame(new_window, height=2, fg_color="white")
    line_frame.place(relx=0.5, rely=0.16, anchor="center", relwidth=1.0)

    vertical_line = CTkFrame(new_window, width=2, fg_color="white")
    vertical_line.place(relx=0.75, rely=0.16, anchor="n", relheight=0.84)

    left_frame = CTkFrame(new_window, width=400, height=750, fg_color="black", corner_radius=10)
    left_frame.place(relx=0.88, rely=0.58, anchor="center")

    instructorname_label = CTkLabel(left_frame, text="Instructors Available", font=("Segoe UI", 20, "bold"), text_color="white")
    instructorname_label.place(relx=0.5, rely=0.1, anchor="center")

    line_frame1 = CTkFrame(left_frame, height=2, fg_color="white")
    line_frame1.place(relx=0.5, rely=0.2, anchor="n", relwidth=1.0)

    gir_sir_checkbox = CTkCheckBox(left_frame, text="Gir Sir", font=("Segoe UI", 16, "bold"), text_color="white", fg_color="#1a73e8")
    gir_sir_checkbox.place(relx=0.5, rely=0.3, anchor="center")

    siddart_sir_checkbox = CTkCheckBox(left_frame, text="Siddart Sir", font=("Segoe UI", 16, "bold"), text_color="white", fg_color="#1a73e8")
    siddart_sir_checkbox.place(relx=0.5, rely=0.4, anchor="center")

    lefty_frame = CTkFrame(new_window, width=910, height=800, fg_color="black", corner_radius=10)
    lefty_frame.place(relx=0.4, rely=0.58, anchor="center")

    try:
        con = sqlite3.connect("databaseexam.db")
        cur = con.cursor()
        con.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")

tooltip = None

root = CTk()
login_frame = CTkFrame(root)
login(root, 'test_username', 'test_password', login_frame)
root.mainloop()
