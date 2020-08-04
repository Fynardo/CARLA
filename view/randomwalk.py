import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


class RandomwalkFrame(tk.Frame):
    def __init__(self, root, controller, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.controller = controller
        self.pack(side=tk.TOP, anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self, text='Simulate randomwalks.')
        self.label.pack()

        self.left_frame = LeftSideFrame(self, borderwidth=2, relief='groove')
        self.left_frame.add_walk_button.bind("<Button>", controller.calculate_walk)
        self.left_frame.reset_button.bind("<Button>", self._reset)

        self.center_frame = CenterFrame(self, borderwidth=2, relief='groove')
        self.center_frame.savefig_button.bind("<Button>", controller.savefig)

    def _reset(self, event=None):
        for frame in [self.left_frame, self.center_frame]:
            frame.reset()                


class LeftSideFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.LEFT, fill=tk.Y)
        _entry_length = 15

        self.walk_length_label = tk.Label(self, text="Length: ")
        self.walk_length_label.pack(side=tk.TOP)
        self.walk_length_entry = tk.Entry(self, width=_entry_length)
        self.walk_length_entry.insert(tk.END, 1000)
        self.walk_length_entry.pack(side=tk.TOP)

        self.steps_label = tk.Label(self, text="Steps: ")
        self.steps_label.pack(side=tk.TOP)
        self.steps_entry = tk.Entry(self, width=_entry_length)
        self.steps_entry.insert(tk.END, '[1, 0, -1]')
        self.steps_entry.pack(side=tk.TOP)

        self.probs_label = tk.Label(self, text="Probs: ")
        self.probs_label.pack(side=tk.TOP)
        self.probs_entry = tk.Entry(self, width=_entry_length)
        self.probs_entry.insert(tk.END, '[0.05, 0.90, 0.05]')
        self.probs_entry.pack(side=tk.TOP)
        
        self.grid_chk_var = tk.IntVar(value=1)
        self.grid_chk = tk.Checkbutton(self, text="Grid", variable=self.grid_chk_var)
        self.grid_chk.pack(side="top")

        self.add_walk_button = tk.Button(self, text="Add Walk")
        self.add_walk_button.pack(side="top", fill=tk.BOTH)
        self.reset_button = tk.Button(self, text="Reset")
        self.reset_button.pack(side="top", fill=tk.BOTH)

    def reset(self):
        self.walk_length_entry.delete(0, tk.END)
        self.walk_length_entry.insert(tk.END, 1000) 

        self.steps_entry.delete(0, tk.END)
        self.steps_entry.insert(tk.END, '[1, 0, -1]')

        self.probs_entry.delete(0, tk.END)
        self.probs_entry.insert(tk.END, '[0.05, 0.90, 0.05]')


class CenterFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.LEFT, anchor=tk.N, fill=tk.X)

        self.up_steps_label = tk.Label(self, text="Up steps: ")
        self.up_steps_label.pack(side=tk.TOP, anchor=tk.NW)

        self.plain_steps_label = tk.Label(self, text="Plain steps: ")
        self.plain_steps_label.pack(side=tk.TOP, anchor=tk.NW)

        self.down_steps_label = tk.Label(self, text="Down steps: ")
        self.down_steps_label.pack(side=tk.TOP, anchor=tk.NW)

        self.fig = Figure(figsize=(10, 7), dpi=80)
        self.ax0 = self.fig.add_axes((0.05, .05, .90, .90), frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP)
        self.canvas.draw()

        self.savefig_button = tk.Button(self, text="Save Figure")
        self.savefig_button.pack(side=tk.LEFT, anchor=tk.W)

        self.savefig_entry = tk.Entry(self, width=70)
        self.savefig_entry.insert(tk.END, os.path.abspath(os.getcwd()) + '/randomwalk.pdf')
        self.savefig_entry.pack(side=tk.LEFT, anchor=tk.W)

    def clear(self):
        self.fig.clear()
        self.ax0 = self.fig.add_axes((0.05, .05, .90, .90), frameon=False)
        self.canvas.draw()

    def redraw(self, x, walk, grid):
        self.ax0.plot(x, walk)        
        self.ax0.grid(grid)
        self.canvas.draw()

    def reset(self):        
        self.clear()
    