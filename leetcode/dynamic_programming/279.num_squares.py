# 279. 完全平方数
import math


def num_squares(n):
    array = [0] * (n + 1)
    for i in range(1, n + 1):
        tmp = n
        for j in range(1, int(math.sqrt(i)) + 1):
            tmp = min(tmp, array[i - j * j] + 1)
        array[i] = tmp
    return array[n]


print(num_squares(12))
print(num_squares(13))
