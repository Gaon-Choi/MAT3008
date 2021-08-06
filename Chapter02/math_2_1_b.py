# 2019009261_Gaon Choi
import math

def f(x):
    return math.exp(-x) + math.cos(x)

a = 1.5
b = 2.0
accuracy = 100
count = 1

f_a = f(a); f_b = f(b)
c_old = b - (f(b)/(f(b)-f(a))) * (b - a)
f_c = f(c_old)
print("#", count)
print("a =", round(a, 5), "b =", round(b, 5), "c_old =", round(c_old, 5), "\n")

while True:
    count += 1
    print("#", count)
    # selection between two interval
    if(f_a * f_c < 0): b = c_old
    elif(f_c * f_b < 0): a = c_old
    print("a =", round(a, 5), "b =", round(b, 5), "c_old =", round(c_old, 5))

    c_new = b - (f(b)/(f(b)-f(a))) * (b - a)
    print("c_new =", round(c_new, 5))
    accuracy = abs(((c_new - c_old)/c_new)) * 100
    c_old = c_new
    print("Accuracy: ", accuracy)
    if(accuracy < 0.0005): break
    print()