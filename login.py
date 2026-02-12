import tkinter as tk
from tkinter import messagebox
import subprocess

#dict of valid users and their passwords
VALID_USERS = {
    "student1": "pass123",
    "student2": "abc456"
}

#function to handle login
def login():

    user = entry_user.get()
    password = entry_pass.get()

    if user in VALID_USERS and VALID_USERS[user] == password:
        root.destroy()
        subprocess.run(["python3", "subprocesstest.py"])
    else:
        messagebox.showerror("Error", "Invalid credentials")


#main window

root = tk.Tk()
root.title("Login")
root.attributes("-fullscreen", True)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="User ID",font=("Helvetica", 50, "bold")).pack()
entry_user = tk.Entry(frame,font=("Helvetica", 50, "bold"))
entry_user.pack()

tk.Label(frame, text="Password", font=("Helvetica", 50, "bold")).pack()
entry_pass = tk.Entry(frame,font=("Helvetica", 50, "bold"), show="*")
entry_pass.pack()

tk.Button(frame, text="Login", font=("Helvetica", 50, "bold"), command=login).pack()

root.mainloop()