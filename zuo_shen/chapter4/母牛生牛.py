def get_n(n):
    if n < 1: return 0
    if n < 5: return n
    return get_n(n - 1) + get_n(n - 3)


def get_n2(n):
    if n < 1: return 0
    if n < 5: return n
    nums = [1, 2, 3]
    for i in range(4, n + 1):
        new_count = nums[-1] + nums[-3]
        nums[0] = nums[1]
        nums[1] = nums[2]
        nums[2] = new_count

    return nums[-1]


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
    base = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
    res = power_matrix2(base, n - 3)
    return 3 * res[0][0] + 2 * res[1][0] + res[2][0]


for i in range(3, 10):
    print("expect", i, get_n(i))
    print("actual", i, get_n2(i))
    print("actual", i, get_n3(i))
