import tkinter as tk
import views
import model


class Presenter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('{}x{}'.format(800, 600))
        self.model = model.Model()
        self.view = views.View(self.root, self.model.get_available_functions())
        self.view.left_side_panel.plot_button.bind("<Button>", self.plot)
        self.view.left_side_panel.clear_button.bind("<Button>", self.clear)

        self.view.top_panel.function_combo.bind("<<ComboboxSelected>>", self.selection_changed)
        self.dynamic_fields = {}
        self.dynamic_labels = []

    def run(self):
        self.root.title("CAldeiro Research LAb, alpha 0.1")
        self.root.deiconify()
        self.root.mainloop()

    def selection_changed(self, event):
        f_name = self.view.top_panel.function_combo.get()
        print(f_name)

        for field in self.dynamic_fields.values():
            field.destroy()

        self.dynamic_fields = {}

        for label in self.dynamic_labels:
            label.destroy()

        print(self.dynamic_fields)
        fields = self.model.get_function_fields(f_name)
        for field in fields:
            item_label = tk.Label(self.view.top_panel.frame, text=field.name+' :')
            item_label.pack(side="left")
            item = field.tk_type(self.view.top_panel.frame, width=10)
            item.insert(tk.END, field.default_value)
            item.pack(side="left")
            self.dynamic_fields[field.name] = item
            self.dynamic_labels.append(item_label)

    def clear(self, event):
        self.view.clear()

    def plot(self, event):
        f_name = self.view.top_panel.function_combo.get()
        x_inf = float(self.view.left_side_panel.x_inf_entry.get())
        x_sup = float(self.view.left_side_panel.x_sup_entry.get())
        step = float(self.view.left_side_panel.step_entry.get())
        print("{}: ({},{},{}). {}".format(f_name, x_inf, x_sup, step, self.view.left_side_panel.grid_chk_var.get()))

        kwargs = {k: v.get() for k,v in self.dynamic_fields.items()}
        print(kwargs)

        x, y = self.model.calculate(f_name, x_inf, x_sup, step, **kwargs)

        self.view.replot(x, y, grid=self.view.left_side_panel.grid_chk_var.get())
