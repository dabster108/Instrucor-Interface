import sqlite3
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkImage, CTkButton, CTkFrame, CTkEntry, CTkComboBox
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
        logoin = CTkImage(dark_image=Image.open("path_to_image/photo00.png"), size=(1920, 1080))
        logoin_right1 = CTkLabel(new_window, image=logoin, text="", fg_color="#333D79")
        logoin_right1.place(relx=0.5, rely=0.5, anchor="center")
    except Exception as e:
        print(f"Error loading background image: {e}")

    try:
        icon = CTkImage(dark_image=Image.open("path_to_image/Book-open_icon-icons.com_52251.ico"), size=(40, 40))
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
     
    # Adding instructor names as labels
    instructor_names = [
        "1. Giri Raj Rawat",
        "2. Manoj Shrestha",
        "3. Siddhartha Neupane",
        "4. Ayush Kaji Dangol"
    ]

    for i, name in enumerate(instructor_names):
        instructor_label = CTkLabel(left_frame, text=name, font=("Segoe UI", 16, "bold"), text_color="white")
        instructor_label.place(relx=0.5, rely=0.25 + i * 0.1, anchor="center")

    lefty_frame = CTkFrame(new_window, width=1020, height=800, fg_color="black", corner_radius=10)
    lefty_frame.place(relx=0.4, rely=0.58, anchor="center")

    vertical_line_in_lefty = CTkFrame(lefty_frame, width=2, fg_color="white")
    vertical_line_in_lefty.place(relx=0.5, rely=0.1, anchor="nw", relheight=0.8)

    student_name_label = CTkLabel(lefty_frame, text="Student Name:", font=("Segoe UI", 16, "bold"), text_color="white")
    student_name_label.place(relx=0.1, rely=0.1, anchor="w")

    student_name_entry = CTkEntry(lefty_frame, width=350, height=40, corner_radius=10, placeholder_text="Enter Student Name", font=("Segoe UI", 16))
    student_name_entry.place(relx=0.1, rely=0.15, anchor="w")

    course_label = CTkLabel(lefty_frame, text="Course:", font=("Segoe UI", 16, "bold"), text_color="white")
    course_label.place(relx=0.1, rely=0.25, anchor="w")

    course_entry = CTkEntry(lefty_frame, width=350, height=40, corner_radius=10, placeholder_text="Enter Course", font=("Segoe UI", 16))
    course_entry.place(relx=0.1, rely=0.3, anchor="w")

    year_label = CTkLabel(lefty_frame, text="Year:", font=("Segoe UI", 16, "bold"), text_color="white")
    year_label.place(relx=0.1, rely=0.4, anchor="w")

    year_entry = CTkEntry(lefty_frame, width=350, height=40, corner_radius=10, placeholder_text="Enter Year", font=("Segoe UI", 16))
    year_entry.place(relx=0.1, rely=0.45, anchor="w")

    instructor_name_label = CTkLabel(lefty_frame, text="Instructor Name:", font=("Segoe UI", 16, "bold"), text_color="white")
    instructor_name_label.place(relx=0.1, rely=0.55, anchor="w")

    instructor_name_combobox = CTkComboBox(lefty_frame, values=instructor_names, font=("Segoe UI", 16, "bold"), width=350, height=40, corner_radius=10)
    instructor_name_combobox.place(relx=0.1, rely=0.6, anchor="w")

    def add_student():
        student_name = student_name_entry.get()
        course = course_entry.get()
        year = year_entry.get()
        instructor_name = instructor_name_combobox.get()
        print(f"Adding student: {student_name}, Course: {course}, Year: {year}, Instructor: {instructor_name}")

    add_student_button = CTkButton(lefty_frame, text="Add Student", width=150, height=40, corner_radius=10, command=add_student)
    add_student_button.place(relx=0.1, rely=0.7, anchor="w")

    def clear_all():
        student_name_entry.delete(0, 'end')
        course_entry.delete(0, 'end')
        year_entry.delete(0, 'end')
        instructor_name_combobox.set('')  # Reset ComboBox

    clear_button = CTkButton(lefty_frame, text="Clear All", width=150, height=40, corner_radius=10, command=clear_all)
    clear_button.place(relx=0.3, rely=0.7, anchor="w")

    new_window.mainloop()

def main():
    root = CTk()
    login_frame = CTkFrame(root)
    login_frame.pack(expand=True, fill='both')

    # Example login UI
    username_label = CTkLabel(login_frame, text="Username", font=("Segoe UI", 16))
    username_label.pack(pady=10)
    
    username_entry = CTkEntry(login_frame, width=250, height=40, placeholder_text="Enter Username")
    username_entry.pack(pady=5)

    password_label = CTkLabel(login_frame, text="Password", font=("Segoe UI", 16))
    password_label.pack(pady=10)
    
    password_entry = CTkEntry(login_frame, width=250, height=40, placeholder_text="Enter Password", show="*")
    password_entry.pack(pady=5)

    login_button = CTkButton(login_frame, text="Login", width=150, height=40, command=lambda: login(root, username_entry.get(), password_entry.get(), login_frame))
    login_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
