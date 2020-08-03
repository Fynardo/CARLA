import tkinter as tk
import numpy as np


class Field:
    def __init__(self, name, default_value, tk_type):
        self.name = name
        self.default_value = default_value
        self.tk_type = tk_type


class BaseFunction:
    fields = []

    def __init__(self, name):
        self.name = name

    def calculate(self, x_inf, x_sup, step, intercept):
        pass


class Linear(BaseFunction):
    fields = [Field('slope', 1, tk.Entry)]

    def __init__(self, slope=None):
        super().__init__('linear')
        self.slope = slope

    def calculate(self, x_inf, x_sup, step, intercept):
        x = np.arange(x_inf, x_sup, step)
        return x, intercept + float(self.slope) * x


class Exponential(BaseFunction):
    def __init__(self):
        super().__init__('exp')

    def calculate(self, x_inf, x_sup, step, intercept):
        x = np.arange(x_inf, x_sup, step)
        return x, intercept + np.exp(x)


class Logarithm(BaseFunction):
    fields = [Field('base', np.e, tk.Entry)]

    def __init__(self, base=None):
        super().__init__('log')
        self.base = base

    def calculate(self, x_inf, x_sup, step, intercept):
        x = np.arange(x_inf, x_sup, step)
        return x, intercept + np.log(x) / np.log(float(self.base))


class NewtonLawCooling(BaseFunction):
    fields = [Field('T', 90, tk.Entry), Field('T0', 10, tk.Entry), Field('theta', 0.027, tk.Entry)]

    def __init__(self, t=None, t0=None, theta=None):
        super().__init__('newton')
        self.t = t
        self.t0 = t0
        self.theta = theta

    def calculate(self, x_inf, x_sup, step, intercept):
        x = np.arange(x_inf, x_sup, step)
        return x, intercept + float(self.t0) + (float(self.t) - float(self.t0)) * np.exp(-float(self.theta) * x)


class Logistic(BaseFunction):
    def __init__(self):
        super().__init__('logistic')

    def calculate(self, x_inf, x_sup, step, intercept):
        x = np.arange(x_inf, x_sup, step)
        return x, intercept + np.exp(x) / (1 + np.exp(x))


