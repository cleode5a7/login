import tkinter as tk
from tkinter import messagebox
import subprocess

#dict of valid users and their passwords
VALID_USERS = ["SNOW"]

class LoginApp:

    #main window

    def __init__(self, root,path_to_experiment):
        self.root = root
        self.path_to_experiment = path_to_experiment
        

        self.frame = tk.Frame(root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame, text="User ID",font=("Helvetica", 50, "bold")).pack()
        self.entry_user = tk.Entry(self.frame,font=("Helvetica", 50, "bold"))
        self.entry_user.pack()

        

        tk.Button(self.frame, text="Login", font=("Helvetica", 50, "bold"), command=self.login).pack()

        

        


    #function to handle login
    def login(self):

        user = self.entry_user.get()
        #change to real path
        script_dir = "/path/to/task_stimuli"
        
        
       

        if user in VALID_USERS:
            self.root.destroy()
            
            subprocess.run(args=["/bin/bash", *self.path_to_experiment.split(' ')], cwd=script_dir, check=True)
        else:
            messagebox.showerror("Error", "Invalid credentials")


    
