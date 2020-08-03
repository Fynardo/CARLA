import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


class GameplayFrame(tk.Frame):
    def __init__(self, root, controller, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.controller = controller
        self.pack(side=tk.TOP, anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self, text='Simulate rolls and gameplay system.')
        self.label.pack()

        self.left_frame = LeftSideFrame(self, borderwidth=2, relief='groove')
        self.left_frame.calculate_button.bind("<Button>", controller.calculate)
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

        self.success_dice_label = tk.Label(self, text="Success Dice: ")
        self.success_dice_label.pack(side=tk.TOP)
        self.success_dice_entry = tk.Entry(self, width=5)
        self.success_dice_entry.insert(tk.END, 10)
        self.success_dice_entry.pack(side=tk.TOP)

        self.success_mod_label = tk.Label(self, text="Success Mod: ")
        self.success_mod_label.pack(side=tk.TOP)
        self.success_mod_entry = tk.Entry(self, width=5)
        self.success_mod_entry.insert(tk.END, 0)
        self.success_mod_entry.pack(side=tk.TOP)

        self.diff_dice_label = tk.Label(self, text="Difficulty Dice: ")
        self.diff_dice_label.pack(side=tk.TOP)
        self.diff_dice_entry = tk.Entry(self, width=5)
        self.diff_dice_entry.insert(tk.END, 10)
        self.diff_dice_entry.pack(side=tk.TOP)

        self.diff_mod_label = tk.Label(self, text="Difficulty Mod: ")
        self.diff_mod_label.pack(side=tk.TOP)
        self.diff_mod_entry = tk.Entry(self, width=5)
        self.diff_mod_entry.insert(tk.END, 0)
        self.diff_mod_entry.pack(side=tk.TOP)

        self.case_label = tk.Label(self, text="Case: ")
        self.case_label.pack(side=tk.TOP)
        self.case_combo = ttk.Combobox(self, width=5, state='readonly')
        self.case_combo["values"] = ['>','>=']
        self.case_combo.pack(side=tk.TOP)
        self.case_combo.current(0)

        self.grid_chk_var = tk.IntVar(value=1)
        self.grid_chk = tk.Checkbutton(self, text="Grid", variable=self.grid_chk_var)
        self.grid_chk.pack(side="top")

        self.calculate_button = tk.Button(self, text="Calculate")
        self.calculate_button.pack(side="top", fill=tk.BOTH)
        self.reset_button = tk.Button(self, text="Reset")
        self.reset_button.pack(side="top", fill=tk.BOTH)

    def reset(self):
        self.success_dice_entry.delete(0, tk.END)
        self.success_dice_entry.insert(tk.END, 10)

        self.success_mod_entry.delete(0, tk.END)
        self.success_mod_entry.insert(tk.END, 0)
        
        self.diff_dice_entry.delete(0, tk.END)
        self.diff_dice_entry.insert(tk.END, 10)

        self.diff_mod_entry.delete(0, tk.END)
        self.diff_mod_entry.insert(tk.END, 0)

        self.case_combo.current(0)


class CenterFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.pack(side=tk.LEFT, anchor=tk.N, fill=tk.X)

        self.total_cases_label = tk.Label(self, text="Total Cases: ")
        self.total_cases_label.pack(side=tk.TOP, anchor=tk.NW)

        self.fav_cases_label = tk.Label(self, text="Fav Cases: ")
        self.fav_cases_label.pack(side=tk.TOP, anchor=tk.NW)

        self.probs_label = tk.Label(self, text="Probs: ")
        self.probs_label.pack(side=tk.TOP, anchor=tk.NW)

        self.fig = Figure(figsize=(10, 7), dpi=80)
        self.ax0 = self.fig.add_axes((0.05, .05, .90, .90), frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP)
        self.canvas.draw()

        self.savefig_button = tk.Button(self, text="Save Figure")
        self.savefig_button.pack(side=tk.LEFT, anchor=tk.W)

        self.savefig_entry = tk.Entry(self, width=70)
        self.savefig_entry.insert(tk.END, os.path.abspath(os.getcwd()) + '/plot.pdf')
        self.savefig_entry.pack(side=tk.LEFT, anchor=tk.W)


    def clear(self):
        self.fig.clear()
        self.ax0 = self.fig.add_axes((0.1, .1, .80, .80), frameon=False)
        self.canvas.draw()

    def redraw(self, z, **kwargs):
        self.clear()
        probs = self.ax0.imshow(z, cmap='RdYlGn')
        self.fig.colorbar(probs)
        self.ax0.set_title(f'Success Probability based on modifiers (d{kwargs["success_dice"].size} vs d{kwargs["diff_dice"].size}) {kwargs["case"]}')
        self.ax0.set_xlabel('Difficulty Modifier')
        self.ax0.set_ylabel('Success Modifier')
        self.ax0.plot(kwargs['diff_dice'].modifier, kwargs['success_dice'].modifier, color='black', marker='x', markersize=16)
        self.canvas.draw()

    def reset(self):
        self.total_cases_label['text'] = "Total Cases: "
        self.fav_cases_label['text'] = "Fav Cases: "
        self.probs_label['text'] = "Probs: "
        self.clear()