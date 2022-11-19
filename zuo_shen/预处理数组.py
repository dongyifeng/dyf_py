# 在一个数组 arr 中，每个数的大小都不超过 1000，例如：[10,9,6,12]，求所有数质数因子的个数求和。


def count_primes(n):
    res = 0
    for i in range(2, round(pow(n, 0.5)) + 1):
        while n % i == 0:
            res += 1
            n /= i
    if n != 1:
        res += 1
    return res


res = []
for i in range(1001):
    res.append(count_primes(i))
print(res)

print(count_primes(180))


def sum_primes(arr):
    bd = [1, 0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3, 1, 3, 2, 2, 1, 4, 2, 2, 3, 3, 1, 3, 1, 5, 2, 2, 2, 4,
          1, 2, 2, 4, 1, 3, 1, 3, 3, 2, 1, 5, 2, 3, 2, 3, 1, 4, 2, 4, 2, 2, 1, 4, 1, 2, 3, 6, 2, 3, 1, 3, 2, 3, 1, 5, 1,
          2, 3, 3, 2, 3, 1, 5, 4, 2, 1, 4, 2, 2, 2, 4, 1, 4, 2, 3, 2, 2, 2, 6, 1, 3, 3, 4, 1, 3, 1, 4, 3, 2, 1, 5, 1, 3,
          2, 5, 1, 3, 2, 3, 3, 2, 2, 5, 2, 2, 2, 3, 3, 4, 1, 7, 2, 3, 1, 4, 2, 2, 4, 4, 1, 3, 1, 4, 2, 2, 2, 6, 2, 2, 3,
          3, 1, 4, 1, 4, 3, 3, 2, 4, 1, 2, 2, 6, 2, 5, 1, 3, 3, 2, 1, 5, 2, 3, 3, 3, 1, 3, 3, 5, 2, 2, 1, 5, 1, 3, 2, 4,
          2, 3, 2, 3, 4, 3, 1, 7, 1, 2, 3, 4, 1, 4, 1, 5, 2, 2, 2, 4, 2, 2, 3, 5, 2, 4, 1, 3, 2, 2, 2, 6, 2, 2, 2, 4, 2,
          3, 1, 6, 4, 2, 1, 4, 1, 3, 3, 4, 1, 4, 2, 3, 2, 3, 1, 6, 1, 3, 5, 3, 3, 3, 2, 4, 2, 4, 1, 5, 2, 2, 3, 8, 1, 3,
          2, 4, 3, 2, 1, 5, 2, 3, 2, 3, 1, 5, 1, 5, 3, 2, 3, 4, 1, 2, 3, 5, 1, 3, 1, 3, 3, 3, 2, 7, 2, 3, 2, 3, 1, 4, 2,
          4, 4, 2, 2, 5, 2, 2, 2, 5, 2, 4, 1, 4, 2, 3, 1, 5, 1, 2, 4, 3, 1, 3, 2, 7, 2, 3, 2, 6, 3, 2, 2, 4, 2, 4, 1, 3,
          3, 2, 2, 6, 1, 3, 2, 4, 2, 4, 3, 4, 3, 2, 1, 4, 1, 4, 4, 6, 1, 3, 2, 3, 3, 2, 1, 6, 2, 2, 3, 4, 2, 3, 1, 5, 3,
          3, 2, 4, 1, 3, 4, 4, 2, 5, 1, 4, 2, 2, 1, 8, 3, 2, 3, 3, 1, 4, 2, 5, 2, 2, 2, 5, 1, 2, 3, 6, 1, 3, 2, 3, 5, 3,
          2, 5, 1, 3, 2, 3, 2, 4, 2, 6, 2, 3, 1, 5, 1, 2, 3, 4, 3, 3, 2, 3, 3, 3, 1, 7, 1, 3, 3, 3, 2, 3, 1, 5, 4, 3, 1,
          4, 2, 2, 2, 7, 1, 5, 2, 3, 2, 2, 3, 5, 1, 2, 4, 4, 1, 4, 1, 5, 3, 2, 1, 5, 2, 3, 2, 4, 2, 3, 3, 4, 3, 2, 1, 7,
          2, 2, 3, 4, 2, 6, 1, 4, 2, 4, 1, 4, 2, 3, 4, 5, 2, 3, 1, 5, 2, 2, 1, 6, 2, 3, 3, 3, 1, 4, 2, 9, 4, 2, 2, 4, 2,
          3, 2, 5, 1, 4, 1, 3, 4, 2, 2, 6, 2, 3, 3, 4, 2, 3, 2, 4, 2, 2, 3, 6, 1, 2, 2, 6, 2, 4, 1, 3, 3, 4, 2, 5, 2, 2,
          3, 3, 1, 4, 2, 6, 3, 2, 1, 4, 2, 2, 5, 4, 1, 4, 1, 4, 2, 3, 3, 8, 1, 3, 2, 4, 2, 3, 2, 4, 4, 2, 1, 5, 2, 3, 2,
          5, 1, 5, 3, 3, 2, 3, 1, 6, 1, 3, 3, 3, 3, 3, 1, 6, 3, 3, 2, 5, 1, 2, 3, 5, 1, 3, 1, 4, 4, 2, 2, 6, 4, 2, 3, 3,
          2, 5, 1, 4, 2, 2, 2, 4, 3, 3, 3, 8, 1, 3, 1, 4, 3, 3, 1, 7, 2, 4, 3, 3, 1, 3, 2, 5, 3, 3, 1, 5, 1, 2, 3, 4, 3,
          4, 2, 3, 2, 3, 2, 7, 1, 2, 5, 4, 1, 3, 2, 5, 2, 3, 1, 5, 2, 4, 2, 5, 2, 4, 1, 3, 4, 2, 2, 5, 2, 2, 2, 5, 1, 5,
          2, 7, 3, 2, 2, 4, 1, 3, 3, 4, 2, 4, 3, 3, 2, 2, 1, 7, 2, 3, 2, 3, 3, 4, 1, 5, 6, 3, 2, 4, 1, 2, 4, 6, 2, 4, 1,
          4, 3, 3, 1, 5, 2, 2, 3, 4, 2, 5, 1, 5, 2, 3, 2, 6, 1, 2, 3, 5, 1, 3, 2, 3, 4, 2, 2, 9, 1, 4, 2, 3, 1, 4, 3, 4,
          3, 2, 2, 5, 2, 3, 4, 6, 2, 3, 1, 3, 2, 3, 2, 6, 2, 2, 3, 3, 1, 4, 2, 7, 3, 2, 2, 4, 3, 3, 2, 4, 1, 6, 1, 4, 2,
          3, 2, 6, 2, 2, 4, 4, 1, 3, 1, 4, 4, 3, 1, 5, 1, 3, 2, 7, 3, 3, 2, 4, 4, 2, 1, 6, 2, 2, 2, 3, 3, 4, 3, 5, 2, 4,
          2, 4, 1, 3, 4, 4, 1, 4, 1, 4, 3, 2, 1, 8, 2, 2, 3, 4, 2, 4, 2, 4, 3, 3, 4, 4, 1, 2, 2, 6, 1, 5, 1, 4, 3, 2, 1,
          5, 2, 3, 5, 3, 2, 3, 2, 8, 3, 2, 2, 6, 2, 3, 3, 4, 2, 3, 1, 3, 3, 4, 1, 6, 2, 2, 3, 3, 2, 5, 1, 5, 2, 2, 2, 5,
          3, 2, 3, 6, 1, 4, 3, 3, 2, 2, 3, 6, 1, 3, 2, 4, 1, 3, 2, 5, 5, 3, 1, 4, 2, 4, 2, 5, 1, 4, 2, 3, 3, 2, 2, 8, 2,
          3, 3, 3, 2, 4, 1, 5, 3, 3, 1, 7, 2, 2, 4, 5, 1, 3, 2, 5, 3, 2, 1, 5, 2, 3, 3, 4, 2, 5, 1, 6, 2, 3, 2, 4, 1, 2,
          4, 6]
    res = 0
    for item in arr:
        res += bd[item]
    return res


print(sum_primes([180, 180]))


def is_m_sum(n):
    for i in range(1, n):
        res = i
        tmp = [i]
        for j in range(i + 1, n):
            res += j
            tmp.append(j)
            if res == n:
                return True
            if res > n:
                break
    return False


import math


def is_m_sum2(n):
    if n == 0: return False
    tmp = math.log(n, 2)
    return tmp != int(tmp)


def is_m_sum3(n):
    if n == 0: return False
    return (n & (n - 1)) != 0


expect = []
actual = []

for i in range(200):
    expect.append(is_m_sum(i))
    actual.append(is_m_sum2(i))
print("result", actual == expect)

'''
牛牛有一些排成一行的正方形。每个正方形已被染成红色或者绿色。牛牛现在可以选择任意一个正方形然后用这两种颜色的任意一种进行染色。
牛牛的目标是在完成染色之后，每个红色 R 都比每个绿色 G 距离最左侧近。牛牛想知道他最少需要涂染几个正方形。
'''

import sys


def min_paint(s):
    if not s or len(s) < 2: return 0
    res = sys.maxsize
    n = len(s)
    for i in range(-1, n):
        # 向寻找左边 G 个数
        left = 0
        k = i
        while k >= 0:
            if s[k] == "G":
                left += 1
            k -= 1

        # 向寻找右边 R 个数
        k = i + 1
        right = 0
        while k < n:
            if s[k] == "R":
                right += 1
            k += 1

        res = min(res, left + right)
    return res


def min_paint2(s):
    if not s or len(s) < 2: return 0

    n = len(s)
    g_count_arr = [0] * (n + 1)
    r_count_arr = [0] * (n + 1)

    for i in range(1, n + 1):
        g_count_arr[i] = g_count_arr[i - 1] + 1 if s[i - 1] == "G" else g_count_arr[i - 1]

    for i in range(n, 0, -1):
        r_count_arr[i - 1] = r_count_arr[i] + 1 if s[i - 1] == "R" else r_count_arr[i]

    res = sys.maxsize
    n = len(s)
    for i in range(-1, n):
        # 向寻找左边 G 个数
        left = g_count_arr[i]
        # 向寻找右边 R 个数
        k = i + 1
        right = r_count_arr[i]
        res = min(res, left + right)
    return res


print("min_paint", min_paint("RGRGR"))
print("min_paint", min_paint("RGGRRGG"))

print("min_paint2", min_paint2("RGRGR"))
print("min_paint2", min_paint2("RGGRRGG"))

'''
给定一个 N * N 的矩阵，只有 0 和 1 两种值，返回边框全是 1 的最大正方形的边长长度。
'''


def max_all_one_border(m):
    n = len(m)
    res = 0
    for row in range(n):
        for col in range(n):

            # 枚举边长
            for border in range(min(n - col, n - row) + 1):
                # 左上点（row，col）边长是 border，验证这样的正方形是不是边框都是 1
                is_one_border = True
                # 验证左边和右边是否全部是 1
                for i in range(row, row + border + 1):
                    if m[i][col] != 1 or m[i][col + border] != 1:
                        is_one_border = False
                        break
                if not is_one_border: continue

                # 验证上边和下边是否全部是 1
                for i in range(col, col + border + 1):
                    if m[row][i] != 1 or m[row + border][i] != 1:
                        is_one_border = False
                        break
                if is_one_border:
                    res = max(res, border + 1)

        return res


print("max_all_one_border", max_all_one_border([[1, 1, 1, 1, 1],
                                                [1, 1, 1, 0, 1],
                                                [0, 1, 0, 1, 1],
                                                [1, 1, 1, 1, 1]]))


def max_all_one_border2(M):
    n = len(M)
    m = len(M[0])
    down = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]

    # 因为填充 right[i][j] 矩阵时，依赖 right[i][j+1]
    # 初始化:right 最后一列的数据
    for i in range(n):
        right[i][-1] = M[i][-1]

    # 因为填充 down[i][j] 矩阵时，依赖 right[i+1][j]
    # 初始化:down 最后一行的数据
    for i in range(m):
        down[-1][i] = M[-1][i]

    # 填充 right 矩阵
    for row in range(n):
        for col in range(m - 2, -1, -1):
            if M[row][col] == 1:
                right[row][col] = right[row][col + 1] + 1
            else:
                right[row][col] = 0

    # 填充 down 矩阵
    for col in range(m):
        for row in range(n - 2, -1, -1):
            if M[row][col] == 1:
                down[row][col] = down[row + 1][col] + 1
            else:
                down[row][col] = 0

    res = 0

    for row in range(n):
        for col in range(m):

            # 枚举边长
            for border in range(min(m - col, n - row)):
                # 左上点（row，col）边长是 border，验证这样的正方形是不是边框都是 1
                # 验证左边和右边是否全部是 1
                is_one_border = right[row][col] >= border and down[row][col] >= border and right[row + border][
                    col] >= border and down[row][col + border] >= border
                if is_one_border:
                    res = max(res, border + 1)

    return res


print(max_all_one_border2([[1, 0, 1, 1, 1],
                           [1, 0, 1, 0, 1],
                           [1, 1, 1, 1, 1],
                           [1, 0, 1, 0, 0]]))

print(max_all_one_border([[1, 0, 1, 1, 1],
                          [1, 0, 1, 0, 1],
                          [1, 1, 1, 1, 1],
                          [1, 0, 1, 0, 0]]))

'''
给定一个函数 f，可以 1 ~ 5 的数字等概率返回一个，请加工出 1 ~ 7 的数字等概率放回一个函数 g
'''
import random


def f():
    return int(random.random() * 5) + 1


def random_01():
    num = f()
    while num == 3:
        num = f()
    return 0 if num < 3 else 1


def g():
    res = 7
    while res == 7:
        res = (random_01() << 2) + (random_01() << 1) + random_01()
    return res + 1


a = [0] * 8
for i in range(100):
    a[g()] += 1

print(a)

'''
给定一个数组 arr，求差值为 k 的去重数字对。
'''


def run(array, k):
    if not array or len(array) < 2:
        return
    num_set = set(array)
    res = set()
    for item in array:
        if item + k in num_set:
            res.add((item, item + k))
    return res


print(run([2, 5, 2, 4, 3, 6, 1], 2))
