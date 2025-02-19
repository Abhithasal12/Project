#pip install customtkinter 
import customtkinter
from tkinter import messagebox
import mysql.connector
from datetime import datetime


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login System")

# Dictionary to store user credentials
USER_CREDENTIALS = {"admin": "1234"}
def login():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="" ,
        # database="my_calculator"
        database="world"
        )
        print(mydb)
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM Login_data")
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
            mycursor.close()
    except mysql.connector.Error as err:
        print('Error', format(err))
        print("Test")

# Function to open sign-up window
def open_signup_window():
    signup_window = customtkinter.CTkToplevel(root)
    signup_window.geometry("400x300")
    signup_window.title("Sign Up")

    customtkinter.CTkLabel(signup_window, text="Create a New Account", font=("Arial", 18)).pack(pady=10)

    new_username_entry = customtkinter.CTkEntry(signup_window, placeholder_text="New Username")
    new_username_entry.pack(pady=8)

    new_password_entry = customtkinter.CTkEntry(signup_window, placeholder_text="New Password", show="*")
    new_password_entry.pack(pady=8)

    # Function to register new user
    def register():
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="" ,
            database="world"
            )
            print(mydb)
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM Login_data")
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
                mycursor.close()
        except mysql.connector.Error as err:
            print('Error', format(err))
            print("Test")
        
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        if new_username in USER_CREDENTIALS:
            messagebox.showerror("Error", "Username already exists! Try another.")
        elif new_username and new_password:
            USER_CREDENTIALS[new_username] = new_password
            messagebox.showinfo("Success", "Account created successfully!")
            signup_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    customtkinter.CTkButton(signup_window, text="Sign Up", command=register).pack(pady=10)

# Create Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Create Label
label = customtkinter.CTkLabel(master=frame, text="Login system", font=("Roboto",24))
label.pack(pady=12, padx=10)

# Username Entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

# Password Entry
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

# Login Button
button= customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

# Message Label (For Error Messages)
message_label = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 14))
message_label.pack(pady=5)

# Checkbox (Remember Me)
checkbox= customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

# Sign-Up Button
signup_button = customtkinter.CTkButton(master=frame, text="Sign Up", command=open_signup_window)
signup_button.pack(pady=10)

root.mainloop()