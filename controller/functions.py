import tkinter as tk
import view.functions as views
import model.functions.service as functions_service


class FunctionsController:
    def __init__(self, view):
        self.view = view  
        self.dynamic_fields = {}
        self.dynamic_labels = []

    #def clear(self):
    #    self.top_panel = None

    def selection_changed(self, event):
        f_name = self.view.main_frame.top_frame.function_combo.get()

        for field in self.dynamic_fields.values():
            field.destroy()

        self.dynamic_fields = {}

        for label in self.dynamic_labels:
            label.destroy()

        fields = functions_service.get_function_fields(f_name)
        for field in fields:
            item_label = tk.Label(self.view.main_frame.top_frame, text=field.name+' :')
            item_label.pack(side="left")
            item = field.tk_type(self.view.main_frame.top_frame, width=10)
            item.insert(tk.END, field.default_value)
            item.pack(side="left")
            self.dynamic_fields[field.name] = item
            self.dynamic_labels.append(item_label)

    def _replot(self, x, y, grid):
        self.view.main_frame.center_frame.clear()
        self.view.main_frame.center_frame.draw(x, y, grid)

    #def _canvas_clear(self, event):
    #    self.clear()

    def canvas_plot(self, event):
        f_name = self.view.main_frame.top_frame.function_combo.get()
        x_inf = float(self.view.main_frame.left_frame.x_inf_entry.get())
        x_sup = float(self.view.main_frame.left_frame.x_sup_entry.get())
        step = float(self.view.main_frame.left_frame.step_entry.get())
        intercept = float(self.view.main_frame.left_frame.intercept_entry.get())

        #kwargs = {k: v.get() for k,v in self.dynamic_fields.items()}
        args = [v.get() for v in self.dynamic_fields.values()]

        x, y = functions_service.calculate(f_name, x_inf, x_sup, step, intercept, *args)

        self._replot(x, y, grid=self.view.main_frame.left_frame.grid_chk_var.get())
