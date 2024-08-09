import sqlite3
from tkinter import messagebox
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkImage, CTkButton, CTkFrame, CTkEntry, CTkComboBox
from PIL import Image
import webbrowser


# Function to create the student database and table
def create_student_db():
    try:
        conn = sqlite3.connect('studentname.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                course TEXT,
                year TEXT,
                instructor_name TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating student database: {e}")

def create_login_db():
    try:
        conn = sqlite3.connect('databaseexam.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                email TEXT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating login database: {e}")

def register_user(fullname, email, username, password):
    try:
        conn = sqlite3.connect('databaseexam.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (fullname, email, username, password) VALUES (?, ?, ?, ?)', (fullname, email, username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        if "UNIQUE constraint failed: users.username" in str(e):
            messagebox.showerror("Error", "Username already exists.")
        else:
            messagebox.showerror("Error", "An error occurred during registration.")

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
        root.destroy()
        open_new_interface(user)
    else:
        error_label = CTkLabel(frame, text="Invalid username or password. Please try again.", font=("Segoe UI", 16, "bold"), text_color="red")
        error_label.place(relx=0.1, rely=0.75, anchor="w")

def open_new_interface(user):
    new_window = CTkToplevel()
    new_window.title("Instructor Management Interface")
    new_window.state('zoomed')
    new_window.iconbitmap("D:\Project Examasap\INSTRUCTOR\Instrucor-Interface\profile.ico")

    # Background image
    try:
        logoin = CTkImage(dark_image=Image.open("D:\Project Examasap\INSTRUCTOR\Instrucor-Interface\Cover (3).png"), size=(1920, 1080))
        logoin_right1 = CTkLabel(new_window, image=logoin, text="")
        logoin_right1.place(relx=0.5, rely=0.5, anchor="center")
    except Exception as e:
        print(f"Error loading background image: {e}")

    # Icon image
    # try:
    #     icon = CTkImage(dark_image=Image.open("path_to_image/Book-open_icon-icons.com_52251.ico"), size=(40, 40))
    #     icon_label = CTkLabel(new_window, image=icon, text="", fg_color="transparent")
    #     icon_label.place(relx=0.05, rely=0.1, anchor="n")
    # except Exception as e:
    #     print(f"Error loading icon image: {e}")

    

    def hide_tooltip(event):
        global tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    def show_description():
        text = ("The Instructor App is a project developed by the talented students of AI Softwarica College. "
            "This innovative interface is designed to connect students with the college's most brilliant teachers, "
            "offering an interactive platform for personalized learning experiences.\n\n"
            "The app features a user-friendly interface built using Tkinter, where students can log in and manage their instructors. "
            "Students have the flexibility to add instructors of their choice, remove them as needed, or update instructor details, "
            "ensuring a dynamic and customized educational journey. The app supports full CRUD (Create, Read, Update, Delete) operations, "
            "making it a comprehensive tool for managing instructor-student interactions.")
        messagebox.showinfo("Description", text,parent = new_window)

    def show_contact():
        text = "Contact: 3108dikshanta@gmail\nNumber: 9843410777"
        messagebox.showinfo("Contact", text,parent = new_window)

    description_button = CTkButton(new_window, text="Description", width=150, height=48, corner_radius=10, fg_color="Yellow", text_color="black", command=show_description)
    description_button.place(relx=0.7, rely=0.1, anchor="nw")

    contact_button = CTkButton(new_window, text="Contact", width=150, height=48, corner_radius=10, fg_color="Yellow", text_color="black", command=show_contact)
    contact_button.place(relx=0.8, rely=0.1, anchor="nw")

    
    
    try:
        profile_icon = CTkImage(dark_image=Image.open("D:\Project Examasap\INSTRUCTOR\Instrucor-Interface\profile.ico"), size=(40, 40))
    except Exception as e:
        print(f"Error loading profile icon image: {e}")
        profile_icon = None  # Fallback in case the icon can't be loaded

    # Profile button
    username = user[3]  # Assuming the username is the fourth element in the user tuple
    profile_button = CTkButton(new_window, text=username, image=profile_icon, compound="left", width=150, height=40, corner_radius=10, fg_color="Yellow", text_color="black")
    profile_button.place(relx=0.9, rely=0.1, anchor="nw")



    


    lefty_frame = CTkFrame(new_window, width=1200, height=800, corner_radius=10,fg_color="black")
    lefty_frame.place(relx=0.4, rely=0.58, anchor="center")

    # try:
    #     lefty_bg_image = CTkImage(dark_image=Image.open("D:\Project Examasap\INSTRUCTOR\Instrucor-Interface\coversss.png"), size=(1200, 800))
    #     lefty_bg_label = CTkLabel(lefty_frame, image=lefty_bg_image, text="", fg_color="transparent")
    #     lefty_bg_label.place(relx=0.5, rely=0.5, anchor="center")
    # except Exception as e:
    #     print(f"Error loading lefty_frame background image: {e}")

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

    instructor_label = CTkLabel(lefty_frame, text="Instructor Name:", font=("Segoe UI", 16, "bold"), text_color="white")
    instructor_label.place(relx=0.1, rely=0.55, anchor="w")

    instructor_names = [
        "Giri Raj Rawat",
        "Manoj Shrestha",
        "Siddhartha Neupane",
        "Ayush Kaji Dangol"
    ]

    instructor_combobox = CTkComboBox(lefty_frame, values=instructor_names, width=350, height=40, corner_radius=10, font=("Segoe UI", 16))
    instructor_combobox.place(relx=0.1, rely=0.6, anchor="w")
    
    
    right_frame = CTkFrame(new_window, width=480, height=750, corner_radius=10,fg_color="gray")
    right_frame.place(relx=0.86, rely=0.58, anchor="center")
    
    resources_label = CTkLabel(right_frame, text="Resources", font=("Segoe UI", 20, "bold"), text_color="white")
    resources_label.place(relx=0.5, rely=0.1, anchor="center")

# Function to open URLs
    def open_resource(url):
        webbrowser.open(url)

    # Buttons for Resources
    resource1_button = CTkButton(right_frame, text="Resource 1", width=200, height=50, corner_radius=10, command=lambda: open_resource("https://www.ibm.com/topics/artificial-intelligence"))
    resource1_button.place(relx=0.5, rely=0.25, anchor="center")

    resource2_button = CTkButton(right_frame, text="Resource 2", width=200, height=50, corner_radius=10, command=lambda: open_resource("https://www.coursera.org/articles/what-is-programming"))
    resource2_button.place(relx=0.5, rely=0.35, anchor="center")

    resource3_button = CTkButton(right_frame, text="Resource 3", width=200, height=50, corner_radius=10, command=lambda: open_resource("https://www.khanacademy.org/computing/computer-programming"))
    resource3_button.place(relx=0.5, rely=0.45, anchor="center")

    resource4_button = CTkButton(right_frame, text="Resource 4", width=200, height=50, corner_radius=10, command=lambda: open_resource("https://www.edx.org/course/introduction-to-computer-science-and-programming"))
    resource4_button.place(relx=0.5, rely=0.55, anchor="center")
        
    

    def add_data():
        student_name = student_name_entry.get()
        course = course_entry.get()
        year = year_entry.get()
        instructor_name = instructor_combobox.get()

        if not (student_name and course and year and instructor_name):
            messagebox.showwarning("Input Error", "All fields are required",parent = new_window)
            return

        try:
            conn = sqlite3.connect('studentname.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (student_name, course, year, instructor_name)
                VALUES (?, ?, ?, ?)
            ''', (student_name, course, year, instructor_name))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data added successfully",parent = new_window)
            update_display(student_name, course, year, instructor_name)
        except Exception as e:
            print(f"Error adding data to student database: {e}")
            messagebox.showerror("Database Error", "Failed to add data",parent = new_window)

    def delete_data():
        student_name = student_name_entry.get()
        course = course_entry.get()
        year = year_entry.get()
        instructor_name = instructor_combobox.get()

        if not (student_name or course or year or instructor_name):
            messagebox.showwarning("Input Error", "At least one field is required to delete data",parent = new_window)
            return

        try:
            conn = sqlite3.connect('studentname.db')
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM students WHERE student_name = ? OR course = ? OR year = ? OR instructor_name = ?
            ''', (student_name, course, year, instructor_name))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data deleted successfully",parent = new_window)
            update_display("", "", "", "")
        except Exception as e:
            print(f"Error deleting data from student database: {e}")
            messagebox.showerror("Database Error", "Failed to delete data",parent=new_window)

    def edit_data():
        student_name = student_name_entry.get()
        course = course_entry.get()
        year = year_entry.get()
        instructor_name = instructor_combobox.get()

        if not (student_name and course and year and instructor_name):
            messagebox.showwarning("Input Error", "All fields are required to update data",parent = new_window)
            return

        try:
            conn = sqlite3.connect('studentname.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET student_name = ?, course = ?, year = ?, instructor_name = ?
                WHERE student_name = ? AND course = ? AND year = ? AND instructor_name = ?
            ''', (student_name, course, year, instructor_name, student_name, course, year, instructor_name))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data updated successfully")
            update_display(student_name, course, year, instructor_name)
        except Exception as e:
            print(f"Error updating data in student database: {e}")
            messagebox.showerror("Database Error", "Failed to update data")

    add_button = CTkButton(lefty_frame, text="Add", command=add_data, width=150, height=40, corner_radius=10)
    add_button.place(relx=0.1, rely=0.75, anchor="w")

    delete_button = CTkButton(lefty_frame, text="Delete", command=delete_data, width=150, height=40, corner_radius=10)
    delete_button.place(relx=0.2, rely=0.75, anchor="w")

    edit_button = CTkButton(lefty_frame, text="Edit", command=edit_data, width=150, height=40, corner_radius=10, fg_color="blue")
    edit_button.place(relx=0.4, rely=0.75, anchor="w")

    # Frame to display the added student data
    display_frame = CTkFrame(lefty_frame, fg_color="gray20", corner_radius=10)
    display_frame.place(relx=0.75, rely=0.3, anchor="center", relwidth=0.35, relheight=0.4)

    def update_display(student_name, course, year, instructor_name):
        for widget in display_frame.winfo_children():
            widget.destroy()

        CTkLabel(display_frame, text="Student Name:", font=("Segoe UI", 16, "bold"), text_color="white").pack(anchor="w", padx=10, pady=5)
        CTkLabel(display_frame, text=student_name, font=("Segoe UI", 16), text_color="white").pack(anchor="w", padx=10)

        CTkLabel(display_frame, text="Course:", font=("Segoe UI", 16, "bold"), text_color="white").pack(anchor="w", padx=10, pady=5)
        CTkLabel(display_frame, text=course, font=("Segoe UI", 16), text_color="white").pack(anchor="w", padx=10)

        CTkLabel(display_frame, text="Year:", font=("Segoe UI", 16, "bold"), text_color="white").pack(anchor="w", padx=10, pady=5)
        CTkLabel(display_frame, text=year, font=("Segoe UI", 16), text_color="white").pack(anchor="w", padx=10)

        CTkLabel(display_frame, text="Instructor Name:", font=("Segoe UI", 16, "bold"), text_color="white").pack(anchor="w", padx=10, pady=5)
        CTkLabel(display_frame, text=instructor_name, font=("Segoe UI", 16), text_color="white").pack(anchor="w", padx=10)

    # Initialize with no data
    update_display("", "", "", "")
