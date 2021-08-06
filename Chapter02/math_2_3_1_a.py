# 2019009261_Gaon Choi
import math
import numpy as np

def f(x):
    return math.exp(x) - 2 * (x ** 2)

def select(x, a, b, c):
    if b >= 0:
        return x - ((2 * c) / (b + math.sqrt(b**2 - 4*a*c)))
    else:   # b < 0
        return x - ((2 * c) / (b - math.sqrt(b**2 - 4*a*c)))

accuracy = math.inf
count = 0
x1 = 1.0; x2 = 2.0; x0 = 1.5


while True:
    print("x1 x0 x2", x1, x0, x2)
    f1 = f(x1)
    f2 = f(x2)
    f0 = f(x0)
    print("f1 f2 f0", f1, f2, f0)
    h1 = x0 - x1; h2 = x2 - x0; r = h2 / h1
    print("h1 h2 r", h1, h2, r)

    a = (r*f1-f0*(1+r)+f2)/(r*h1*h1*(1+r))
    b = (a*h1*h1+f0-f1)/h1
    c = f0
    print("a b c", a, b, c)

    x3_temp = x0
    x0_temp = x0
    x3 = select(x0, a, b, c)
    print(x3)
    print(np.floor(x3 * (10**5))/(10**5))

    if x3 < x0:
        x0 = x3; x2 = x0_temp
    else:
        x0 = x3; x1 = x0_temp
    print("x1 x0 x2", x1, x0, x2)
    accuracy = abs((x3 - x0_temp)/x3) * 100
    print("Accuracy: ", accuracy)
    print()
    if(accuracy < 0.00005):
        break