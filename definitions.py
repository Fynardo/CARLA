import tkinter as tk
import numpy as np


class Field:
    def __init__(self, name, default_value, tk_type):
        self.name = name
        self.default_value = default_value
        self.tk_type = tk_type


class Linear:
    def __init__(self):
        self.name = 'linear'
        self.fields = [Field('intercept', 0, tk.Entry), Field('slope', 1, tk.Entry)]

    def calculate(self, x_inf, x_sup, step, intercept, slope):
        x = np.arange(x_inf, x_sup, step)
        return x, float(intercept) + float(slope) * x


class Exponential:
    def __init__(self):
        self.name = 'exp'
        self.fields = []

    def calculate(self, x_inf, x_sup, step):
        x = np.arange(x_inf, x_sup, step)
        return x, np.exp(x)


class Logarithm:
    def __init__(self):
        self.name = 'log'
        self.fields = [Field('base', np.e, tk.Entry)]

    def calculate(self, x_inf, x_sup, step, base):
        x = np.arange(x_inf, x_sup, step)
        return x, np.log(x) / np.log(float(base))


class NewtonLawCooling:
    def __init__(self):
        self.name = 'newton'
        self.fields = [Field('T', 90, tk.Entry), Field('T0', 10, tk.Entry), Field('theta', 0.027, tk.Entry)]

    def calculate(self, x_inf, x_sup, step, T, T0, theta):
        x = np.arange(x_inf, x_sup, step)

        return x, int(T0) + (int(T) - int(T0)) * np.exp(-float(theta) * x)


class Logistic:
    def __init__(self):
        self.name = 'logistic'
        self.fields = []

    def calculate(self, x_inf, x_sup, step):
        x = np.arange(x_inf, x_sup, step)

        return x, np.exp(x) / (1 + np.exp(x))


functions = {'exp': Exponential, 'linear': Linear, 'log': Logarithm, 'logistic': Logistic, 'newton': NewtonLawCooling}


def get_function(f_name, *kwargs):
    for k, v in functions.items():
        if k == f_name:
            return v(*kwargs)


def get_function_names():
    return [k for k in functions.keys()]
