from .definitions import *


function_builder = {'exp': Exponential, 'linear': Linear, 'log': Logarithm, 'logistic': Logistic, 'newton': NewtonLawCooling}


def _get_function(f_name):
    for k, v in function_builder.items():
        if k == f_name:
            return v


def _create_function(f_name, *args):
    for k, v in function_builder.items():
        if k == f_name:
            return v(*args)


def get_available_functions():
    return [k for k in function_builder.keys()]


def get_function_fields(f_name):
    f = _get_function(f_name)
    return f.fields


def calculate(f_name, x_inf, x_sup, step, intercept, *args):
    f = _create_function(f_name, *args)
    return f.calculate(x_inf, x_sup, step, intercept)
