import definitions


class Model:
    def __init__(self):
        pass

    def get_available_functions(self):
        return definitions.get_function_names()

    def get_function_fields(self, f_name):
        f = definitions.get_function(f_name)
        return f.fields

    def calculate(self, f_name, x_inf, x_sup, step, intercept, *args):
        f = definitions.create_function(f_name, *args)
        return f.calculate(x_inf, x_sup, step, intercept)








