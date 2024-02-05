import numpy as np


def f(x):
    return x ** 5 + 2 * x + 1


raizes = np.roots([1, 0, 0, 0, 2, 1])

print("Raízes encontradas:", raizes)
