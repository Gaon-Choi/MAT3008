# 2019009261 Gaon Choi

import numpy as np

a = np.array([-8, 3, 1, -4])
b = np.array([2, -6, -1, -3])
c = np.array([1, 1, -3, 5])

count = 1
x1_temp = 1/4
x2_temp = -1/2
x3_temp = -1/4
# print("#",count,": ", x1_temp, x2_temp, x3_temp)
# count += 1
criteria = 0.5 * (10 ** (2-5))


while True:
    x1 = (1/4) * (1-x2_temp)
    x2 = (-1/4) * (2-(x1_temp + x3_temp))
    x3 = (1/4) * (-1 - x2_temp)
    print("#", count, ": ", x1_temp, x2_temp, x3_temp)
    count += 1
    accuracy_1 = abs(((x1 - x1_temp) / x1) * 100)
    accuracy_2 = abs(((x2 - x2_temp) / x2) * 100)
    accuracy_3 = abs(((x3 - x3_temp) / x3) * 100)
    x1_temp = x1; x2_temp = x2; x3_temp = x3
    if(accuracy_1 <= criteria and accuracy_2 <= criteria and accuracy_3 <= criteria): break;