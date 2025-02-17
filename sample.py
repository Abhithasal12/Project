# import customtkinter
# from tkinter import messagebox

# # Set theme
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# # Dictionary to store user credentials
# USER_CREDENTIALS = {"admin": "1234"}

# # Function to toggle password visibility
# def toggle_password():
#     if entry2.cget("show") == "*":
#         entry2.configure(show="")
#         toggle_btn.configure(text="Hide")
#     else:
#         entry2.configure(show="*")
#         toggle_btn.configure(text="Show")

# # Function to validate login
# def login():
#     username = entry1.get()
#     password = entry2.get()

#     if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#         message_label.configure(text="Login Successful ✅", text_color="green")
#     else:
#         message_label.configure(text="Invalid Username or Password ❌", text_color="red")

# # Function to open sign-up window
# def open_signup_window():
#     signup_window = customtkinter.CTkToplevel(root)
#     signup_window.geometry("400x300")
#     signup_window.title("Sign Up")

#     customtkinter.CTkLabel(signup_window, text="Create a New Account", font=("Arial", 18)).pack(pady=10)

#     new_username_entry = customtkinter.CTkEntry(signup_window, placeholder_text="New Username")
#     new_username_entry.pack(pady=8)

#     new_password_entry = customtkinter.CTkEntry(signup_window, placeholder_text="New Password", show="*")
#     new_password_entry.pack(pady=8)

#     # Function to register new user
#     def register():
#         new_username = new_username_entry.get()
#         new_password = new_password_entry.get()

#         if new_username in USER_CREDENTIALS:
#             messagebox.showerror("Error", "Username already exists! Try another.")
#         elif new_username and new_password:
#             USER_CREDENTIALS[new_username] = new_password
#             messagebox.showinfo("Success", "Account created successfully!")
#             signup_window.destroy()
#         else:
#             messagebox.showerror("Error", "Please fill in all fields.")

#     customtkinter.CTkButton(signup_window, text="Sign Up", command=register).pack(pady=10)

# # Create main window
# root = customtkinter.CTk()
# root.geometry("500x400")
# root.title("Login System")

# # Create Frame
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# # Create Label
# label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Arial", 24))
# label.pack(pady=12, padx=10)

# # Username Entry
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)

# # Password Entry
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry2.pack(pady=12, padx=10)

# # Show/Hide Password Button
# toggle_btn = customtkinter.CTkButton(master=frame, text="Show", command=toggle_password, width=10)
# toggle_btn.pack(pady=5)

# # Login Button
# button = customtkinter.CTkButton(master=frame, text="Login", command=login)
# button.pack(pady=12, padx=10)

# # Message Label (For Error Messages)
# message_label = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 14))
# message_label.pack(pady=5)

# # Checkbox (Remember Me)
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=8)

# # Sign-Up Button
# signup_button = customtkinter.CTkButton(master=frame, text="Sign Up", command=open_signup_window)
# signup_button.pack(pady=10)   

# # Run the main loop
# root.mainloop()


import tkinter as tk
import mysql.connector
from datetime import datetime

# Connect to the database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="my_calculator"
)

# Initialize cursor (we'll open it when needed)
mycursor = mydb.cursor()

calculation = ""

def add_to_calculation(symbol):
    global calculation
    if symbol == "%":
        calculation += "*10/100"
    else:
        calculation += str(symbol)

    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    print(calculation)
    try:
        result = str(eval(calculation))
        calculation = ""  # Reset calculation after evaluating
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)

        # Insert calculation and result into the database
        sql = "INSERT INTO History (expression, result, created_at) VALUES (%s, %s, %s)"
        val = (calculation, result, datetime.now())
        
        # Open cursor for executing the query
        mycursor.execute(sql, val)
        mydb.commit()
        print("Record inserted successfully!")

    except Exception as e:
        clear_filed()
        text_result.insert(1.0, "Error")
        print(f"Error: {e}")

def clear_filed():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Delete button
def delete_filed():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Create the main window (Tkinter)
root = tk.Tk()
root.geometry("300x325")
root.title("Calculator")

# Text field to display the calculation result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), background="Gray")
text_result.grid(columnspan=5)

# Buttons for numbers, operations, and functionality
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('0', 5, 2),
    ('+', 2, 4), ('-', 3, 4), ('*', 4, 4), ('/', 5, 4),
    ('.', 5, 3), ('00', 5, 1), ('%', 6, 1)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14), background="yellow").grid(row=row, column=col)

# Special buttons
tk.Button(root, text="DEL", command=delete_filed, width=11, font=("Arial", 14), background="orange").grid(row=6, column=3, columnspan=2)
tk.Button(root, text="C", command=clear_filed, width=11, font=("Arial", 14), background="orange").grid(row=7, column=1, columnspan=2)
tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14), background="orange").grid(row=7, column=3, columnspan=2)

root.mainloop()
