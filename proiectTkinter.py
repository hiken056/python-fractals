import tkinter as tk
import colorsys

class FractalDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Drawer")

        self.fractal_types = ["Mandelbrot", "Julia", "Dragon"]
        self.selected_fractal = tk.StringVar(value=self.fractal_types[0])

        self.create_widgets()

    def create_widgets(self):
        # Fractal type dropdown
        type_label = tk.Label(self.root, text="Select Fractal Type:")
        type_dropdown = tk.OptionMenu(self.root, self.selected_fractal, *self.fractal_types)
        type_dropdown.grid(row=0, column=0, pady=10)
        type_label.grid(row=0, column=1, pady=10)

        # Draw button
        draw_button = tk.Button(self.root, text="Draw Fractal", command=self.draw_fractal)
        draw_button.grid(row=0, column=2, pady=10)

        # Clear button
        clear_button = tk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
        clear_button.grid(row=0, column=3, pady=10)

        # Canvas widget for drawing
        self.canvas = tk.Canvas(self.root, width=1200, height=800, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=4, pady=10)

    def draw_fractal(self):
        fractal_type = self.selected_fractal.get()

        if fractal_type == "Mandelbrot":
            self.draw_mandelbrot()
        elif fractal_type == "Julia":
            self.draw_julia()
        elif fractal_type == "Dragon":
            self.draw_dragon()

    def draw_mandelbrot(self):
        self.canvas.delete("all")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        max_iter = 100

        for y in range(height):
            self.root.update()

            for x in range(width):
                zx, zy = x * (3.0 / width) - 2, y * (2.0 / height) - 1
                c = zx + zy * 1j
                z = c
                color = self.mandelbrot_color(z, c, max_iter)
                if color == "#000000":
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

    def mandelbrot_color(self, z, c, max_iter=100):
        for i in range(max_iter):
            if abs(z) > 2.0:
                return "#000000"
            z = z * z + c
        return "#FFFFFF"

    def draw_julia(self):
        self.canvas.delete("all")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        max_iter = 100
        julia_constant = complex(-0.7, 0.27015)

        for y in range(height):
            self.root.update()

            for x in range(width):
                zx, zy = x * (3.0 / width) - 2, y * (2.0 / height) - 1
                z = complex(zx, zy)
                color = self.julia_color(z, julia_constant, max_iter)
                if color == "#000000":
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

    def julia_color(self, z, c, max_iter=100):
        for i in range(max_iter):
            if abs(z) > 2.0:
                return "#000000"
            z = z * z + c
        return "#FFFFFF"

    def draw_dragon(self):
        self.canvas.delete("all")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        max_iter = 500

        for y in range(height):
            self.root.update()

            for x in range(width):
                zx, zy = x * (3.0 / width) - 2, y * (2.0 / height) - 1
                c = complex(-0.5, 0.5)
                z = complex(zx, zy)
                color = self.dragon_color(z, c, max_iter)
                if color == "#000000":
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

    def dragon_color(self, z, c, max_iter=500):
        for i in range(max_iter):
            if abs(z) > 2.0:
                return "#000000"
            z = complex(z.real**2 - z.imag**2 + c.real, 2 * z.real * z.imag + c.imag)
        return "#FFFFFF"

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalDrawer(root)
    root.mainloop()
