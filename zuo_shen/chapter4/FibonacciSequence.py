# 给定整数 N，返回斐波那契数列的 第 N 项。

# O(N^2)
def get_n(n):
    if n < 1: return 0
    if n < 3: return 1
    return get_n(n - 1) + get_n(n - 2)


# O(N)
def get_n2(n):
    if n < 1: return 0
    if n < 3: return 1

    num1 = 1
    num2 = 1
    res = 0
    for i in range(2, n):
        res = num1 + num2
        num1 = num2
        num2 = res
    return res


def get_n4(n):
    if n < 1: return 0
    if n < 3: return 1

    num1 = num2 = 1
    for i in range(2, n):
        num2, num1 = num1 + num2, num2
    return num2


print(get_n4(10))
print(get_n2(10))


def product_matrix(M, N):
    m_row = len(M)
    n_col = len(N[0])
    res = [[0] * (n_col) for _ in range(m_row)]

    for k in range(m_row):
        for i in range(n_col):
            for j in range(m_row):
                res[k][i] += M[k][j] * N[j][i]
    return res


def power_matrix(M, n):
    res = [[0] * (len(M[0])) for _ in range(len(M))]
    for i in range(min(len(M[0]), len(M))):
        res[i][i] = 1
    p = n
    tmp = M
    while p != 0:
        if p & 1 != 0:
            res = product_matrix(res, tmp)
        tmp = product_matrix(tmp, tmp)
        p >>= 1
    return res


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
    tmp = power_matrix2(base, n - 2)
    return sum(tmp[0])


import numpy as np

a = np.array([[1, 2], [1, 2]])
b = np.array([[1, 2], [1, 2]])

print("np.power", np.power(a, 2))

print(np.dot(a, b))

print("product_matrix", product_matrix([[3, 6], [3, 6]], [[1, 2], [1, 2]]))

print("pow_matrix", power_matrix([[1, 2], [1, 2]], 3))

print(product_matrix([[1, 2], [3, 4]], [[1, 2, 3], [1, 2, 3]]))


print("get_n2",get_n2(10))
print("get_n2",get_n3(10))

# O(logN)

def test():
    for i in range(20):
        expect = get_n(i)
        actual = get_n2(i)
        if expect != actual:
            print(i, expect, actual)


test()
