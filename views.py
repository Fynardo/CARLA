import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View:
    def __init__(self, master, entries):
        self.frame = tk.Frame(master)

        self.top_panel = TopPanel(master, entries)
        self.left_side_panel = LeftSidePanel(master)
        self.right_side_panel = RightSidePanel(master)
        self.canvas_panel = CanvasPanel(master)

    def plot(self, x, y, grid):
        self.canvas_panel.draw(x, y, grid)

    def clear(self):
        self.canvas_panel.clear()

    def replot(self, x, y, grid):
        self.clear()
        self.plot(x, y, grid)


class TopPanel:
    def __init__(self, root, entries):
        self.frame = tk.Frame(root, height=50)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.frame.pack_propagate(0)

        self.function_label = tk.Label(self.frame, text="Function: ")
        self.function_label.pack(side="left")
        self.function_combo = ttk.Combobox(self.frame, width=10)
        self.function_combo["values"] = entries

        self.function_combo.pack(side="left")


class LeftSidePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root, width=100)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.frame.pack_propagate(0)

        self.x_inf_label = tk.Label(self.frame, text="X_inf: ")
        self.x_inf_label.pack(side="top")
        self.x_inf_entry = tk.Entry(self.frame)
        self.x_inf_entry.insert(tk.END, 1)
        self.x_inf_entry.pack(side="top")

        self.x_sup_label = tk.Label(self.frame, text="X_sup: ")
        self.x_sup_label.pack(side="top")
        self.x_sup_entry = tk.Entry(self.frame)
        self.x_sup_entry.insert(tk.END, 100)
        self.x_sup_entry.pack(side="top")

        self.step_label = tk.Label(self.frame, text="Step: ")
        self.step_label.pack(side="top")
        self.step_entry = tk.Entry(self.frame)
        self.step_entry.insert(tk.END, 1)
        self.step_entry.pack(side="top")

        self.grid_chk_var = tk.IntVar(value=1)
        self.grid_chk = tk.Checkbutton(self.frame, text="Grid", variable=self.grid_chk_var)
        self.grid_chk.pack(side="top")

        self.plot_button = tk.Button(self.frame, text="Plot ")
        self.plot_button.pack(side="top", fill=tk.BOTH)
        self.clear_button = tk.Button(self.frame, text="Clear")
        self.clear_button.pack(side="top", fill=tk.BOTH)


class CanvasPanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.fig = Figure(figsize=(7.5, 4), dpi=80)
        self.ax0 = self.fig.add_axes((0.05, .05, .90, .90), frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

    def draw(self, x, y, grid):
        self.ax0.plot(x, y)
        if grid:
            self.ax0.grid()
        self.canvas.draw()

    def clear(self):
        self.ax0.clear()
        self.canvas.draw()


class RightSidePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root, width=100)
        self.frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.frame.pack_propagate(0)

        self.x_inf_label = tk.Label(self.frame, text="Attribute: ")
        self.x_inf_label.pack(side="top")
