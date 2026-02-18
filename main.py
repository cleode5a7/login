import tkinter as tk
from login import LoginApp

def main():
    root = tk.Tk()
    root.title("Login")
    root.attributes("-fullscreen", True)

    #replace "subprocesstest.py" with the path to your actual experiment script
    LoginApp(
    root,
    script_path="/home/cleo/Desktop/project/run_docker.sh",
    script_args=["--rom", "rom1.nes"])


    root.mainloop()

if __name__ == "__main__":
    main()
