import numpy as np

def simulate_steps(steps, n, p):
    return np.random.choice(a=steps, size=n, p=p)

def simulate_walk(steps, n, p):
    return simulate_steps(steps, n, p).cumsum(0)

