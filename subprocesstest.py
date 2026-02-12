import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Big Heart wow!")
root.geometry("800x600")

# Create canvas to draw on
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

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
