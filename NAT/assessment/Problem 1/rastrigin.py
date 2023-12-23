import numpy as np


def rastrigin_func(x):
    '''
    Define the Rastrigin Function.
    '''
    return 10 * len(x) + sum([(xi**2 - 10 * np.cos(2 * np.pi * xi)) for xi in x])