import tkinter as tk
from tkinter import ttk
import view.main


class MainFrame(tk.Frame):
    def __init__(self, root, controller, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.controller = controller
        self.pack(fill=tk.BOTH)

        self.selection_frame = view.main.SelectionFrame(self)
        self.selection_frame.pack(fill=tk.X)
        self.selection_frame.utilities_combo.bind("<<ComboboxSelected>>", controller.selection_changed)

    def set_main_frame(self, frame):
        self.main_frame = frame


class SelectionFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.utilities_label = tk.Label(self, text="Select Utility: ")
        self.utilities_label.pack(side=tk.LEFT)

        self.utilities_combo = ttk.Combobox(self, width=15, state='readonly')
        self.utilities_combo["values"] = ['Gameplay', 'Randomwalk', 'Functions']
        self.utilities_combo.current(0)
        self.utilities_combo.pack(side=tk.LEFT)    
