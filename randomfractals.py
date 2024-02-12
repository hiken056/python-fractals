import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle, ScrolledCanvas
import random

fractals = {
    "Koch Snowflake": ("F--F--F", {"F": "F+F--F+F"}, 4, 60),
    "Dragon Curve": ("FX", {"X": "X+YF+", "Y": "-FX-Y"}, 10, 90),
    "Hilbert Curve": ("L", {"L": "-RF+LFL+FR-", "R": "+LF-RFR-FL+"}, 4, 90),
    "Peano-Gosper Curve": ("FX", {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}, 4, 60),
    "Levy C Curve": ("F", {"F": "+F--F+"}, 10, 45),
    "Sierpinski Arrowhead Curve": ("YF", {"X": "YF+XF+Y", "Y": "XF-YF-X"}, 5, 60),
    "Terdragon Curve": ("F", {"F": "F+F-F"}, 6, 120),
    "Pentaplexity": ("F++F++F++F++F", {"F": "F++F++F+++++F-F++F"}, 2, 36),
    "Cross Curve": ("F", {"F": "F+F-F-F+F"}, 4, 90),
    "Sierpinski Hexagon": ("F+F+F+F+F+F", {"F": "F-F+F+F-F"}, 3, 60),
    "Hexagonal Gosper Curve": ("F", {"F": "F-G--G+F+F-G--G+F-F+F+G--G-F+F-G--G+"}, 3, 60),
    "Square Dragon Curve": ("FX+FX+FX+FX+", {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}, 4, 90),
}

def apply_rules(ch, rules):
    return rules.get(ch, ch)

def iterate(sequence, rules):
    return ''.join(apply_rules(ch, rules) for ch in sequence)

def draw_fractal(axiom, rules, iterations, turtle, scale=10, angle=90):
    sequence = axiom
    for _ in range(iterations):
        sequence = iterate(sequence, rules)

    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    for element in sequence:
        if element == "F":
            turtle.forward(scale)
        elif element == "+":
            turtle.right(angle)
        elif element == "-":
            turtle.left(angle)

def clear_canvas(turtle):
    turtle.clear()

def random_fractal():
    return random.choice(list(fractals.values()))

def draw_random_fractal(turtle):
    axiom, rules, iterations, angle = random_fractal()
    draw_fractal(axiom, rules, iterations, turtle, angle=angle)

def draw_selected_fractal(selected_fractal_var, turtle):
    selected_fractal = selected_fractal_var.get()

    if selected_fractal in fractals:
        axiom, rules, iterations, angle = fractals[selected_fractal]
        draw_fractal(axiom, rules, iterations, turtle, angle=angle)

def create_gui():
    root = tk.Tk()
    root.title("Fractal Drawer")

    canvas = ScrolledCanvas(root)
    canvas.pack(expand=True, fill="both")
    turtle = RawTurtle(canvas)
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.color("#ff69aa")

    draw_button = tk.Button(root, text="Draw Random Fractal", command=lambda: draw_random_fractal(turtle))
    draw_button.pack(pady=10)

    clear_button = tk.Button(root, text="Clear Canvas", command=lambda: clear_canvas(turtle))
    clear_button.pack(pady=10)

    fractal_var = tk.StringVar()
    fractal_var.set("Select Fractal")

    fractal_dropdown = ttk.Combobox(root, textvariable=fractal_var, values=list(fractals.keys()))
    fractal_dropdown.pack(pady=10)

    draw_selected_button = tk.Button(root, text="Draw Selected Fractal", command=lambda: draw_selected_fractal(fractal_var, turtle))
    draw_selected_button.pack(pady=10)

    root.mainloop()


create_gui()
