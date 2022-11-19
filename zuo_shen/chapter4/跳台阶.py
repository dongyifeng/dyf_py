def get_n(n):
    if n < 1: return 0
    if n < 3: return n
    return get_n(n - 1) + get_n(n - 2)


def get_n2(n):
    if n < 1: return 0
    if n < 3: return n
    num1 = 1
    num2 = 2
    for i in range(2, n):
        num2, num1 = num1 + num2, num2
    return num2


import numpy as np


def power_matrix2(M, n):
    res = np.identity(len(M))
    p = n
    tmp = M
    while p != 0:
        if p & 1 != 0:
            res = np.dot(res, tmp)
        tmp = np.dot(tmp, tmp)
        p >>= 1
    return res


def get_n3(n):
    if n < 1: return 0
    if n < 3: return 1
    base = [[1, 1], [1, 0]]
    res = power_matrix2(base, n - 2)
    # [2,1] * res
    return 2 * res[0][0] + res[1][0]


for i in range(3, 10):
    print("expect", get_n(i))
    print("actual", get_n2(i))
    print("actual", get_n3(i))
