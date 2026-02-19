import tkinter as tk
from login import LoginApp

def main():
    root = tk.Tk()
    root.title("Login")
    root.attributes("-fullscreen", True)

    #replace with the path to your actual experiment script and flags
    LoginApp(
    root, "docker/run_docker.sh --subject 01 --session 001 --output /tmp/mario --tasks mario")


    root.mainloop()

if __name__ == "__main__":
    main()
