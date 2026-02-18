import tkinter as tk
from tkinter import messagebox
import subprocess

#dict of valid users and their passwords
VALID_USERS = ["SNOW"]

class LoginApp:

    #main window

    def __init__(self, root,path_to_experiment, script_args=None):
        self.root = root
        self.path_to_experiment = path_to_experiment
        self.script_args = None or []

        self.frame = tk.Frame(root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="User ID",font=("Helvetica", 50, "bold")).pack()
        self.entry_user = tk.Entry(self.frame,font=("Helvetica", 50, "bold"))
        self.entry_user.pack()

        

        tk.Button(self.frame, text="Login", font=("Helvetica", 50, "bold"), command=self.login).pack()

        

        


    #function to handle login
    def login(self):

        user = self.entry_user.get()
        script_dir = os.path.dirname(self.script_path)

        subprocess.run(
        ["bash", self.script_path] + self.script_args,
        cwd=script_dir,
        check=True
        )

        
       

        if user in VALID_USERS:
            self.root.destroy()
            
            subprocess.run(["python3", self.path_to_experiment])
        else:
            messagebox.showerror("Error", "Invalid credentials")


    
