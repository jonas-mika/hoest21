import numpy as np
xs = list(range(100))


def f(x):
    return (x-40)**2


ys = [f(x) for x in xs]

guess = 50
res = ys[guess]
print(res)

guess = 75
res = ys[guess]

print(res)
