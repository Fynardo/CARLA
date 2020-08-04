import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FunctionsFrame(tk.Frame):
    def __init__(self, root, controller, function_values, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.controller = controller
        self.pack(side=tk.TOP, anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self, text='Common functions behavior and simulation.')
        self.label.pack()

        self.top_frame = TopFrame(self, function_values, borderwidth=2, relief='groove')
        self.left_frame = LeftFrame(self, borderwidth=2, relief='groove')
        self.center_frame = CanvasFrame(self, borderwidth=2, relief='groove')

        self.left_frame.plot_button.bind("<Button>", self.controller.canvas_plot)
        self.left_frame.clear_button.bind("<Button>", self.center_frame.clear)

        self.top_frame.function_combo.bind("<<ComboboxSelected>>", self.controller.selection_changed)


class TopFrame(tk.Frame):
    def __init__(self, root, function_values, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X)

        self.function_label = tk.Label(self, text="Function: ")
        self.function_label.pack(side=tk.LEFT)
        self.function_combo = ttk.Combobox(self, width=10, state='readonly')
        self.function_combo["values"] = function_values
        #self.function_combo.current(0)

        self.function_combo.pack(side=tk.LEFT)


class LeftFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.LEFT, anchor=tk.NW)

        self.x_inf_label = tk.Label(self, text="X_inf: ")
        self.x_inf_label.pack(side=tk.TOP)
        self.x_inf_entry = tk.Entry(self, width=5)
        self.x_inf_entry.insert(tk.END, 1)
        self.x_inf_entry.pack(side=tk.TOP)

        self.x_sup_label = tk.Label(self, text="X_sup: ")
        self.x_sup_label.pack(side=tk.TOP)
        self.x_sup_entry = tk.Entry(self, width=5)
        self.x_sup_entry.insert(tk.END, 100)
        self.x_sup_entry.pack(side=tk.TOP)

        self.step_label = tk.Label(self, text="Step: ")
        self.step_label.pack(side=tk.TOP)
        self.step_entry = tk.Entry(self, width=5)
        self.step_entry.insert(tk.END, 1)
        self.step_entry.pack(side=tk.TOP)

        self.intercept_label = tk.Label(self, text="Intercept: ")
        self.intercept_label.pack(side=tk.TOP)
        self.intercept_entry = tk.Entry(self, width=5)
        self.intercept_entry.insert(tk.END, 0)
        self.intercept_entry.pack(side=tk.TOP)

        self.grid_chk_var = tk.IntVar(value=1)
        self.grid_chk = tk.Checkbutton(self, text="Grid", variable=self.grid_chk_var)
        self.grid_chk.pack(side=tk.TOP)

        self.plot_button = tk.Button(self, text="Plot ")
        self.plot_button.pack(side=tk.TOP, fill=tk.BOTH)
        self.clear_button = tk.Button(self, text="Clear")
        self.clear_button.pack(side=tk.TOP, fill=tk.BOTH)


class CanvasFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.LEFT)
        self.fig = Figure(figsize=(10, 7), dpi=80)
        self.ax0 = self.fig.add_axes((0.05, .05, .90, .90), frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

    def draw(self, x, y, grid):
        self.ax0.plot(x, y)
        if grid:
            self.ax0.grid(True)
        self.canvas.draw()

    def clear(self, event=None):
        self.fig.clear()
        self.ax0 = self.fig.add_axes((0.05, 0.05, .90, .90), frameon=False)
        self.canvas.draw()
