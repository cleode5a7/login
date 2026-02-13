import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Big Heart wow!")
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Create canvas to draw on
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
canvas.pack()

tk.Label(root, text="I LOVE YOU, LISTEN TO THE FEMCELS", font=("Helvetica", 50, "bold"), fg="red").place(relx=0.5, rely=0.1, anchor="center")
# Draw a heart shape using polygon coordinates
heart_points = [
    400, 450,   # bottom tip
    250, 300,
    200, 200,
    250, 150,
    350, 200,
    400, 300,
    450, 200,
    550, 150,
    600, 200,
    550, 300
]

canvas.create_polygon(
    heart_points,
    fill="pink",
    outline="black",
    width=3,
    smooth=True
)


root.mainloop()
