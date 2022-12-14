'''
给定 n 种物品和一背包。物品 i 的重量是 $w_i$，其价值为$v_i$ ，背包的容量为 C。问应如何选择装入背包的物品，使得装入背包中物品的总价值最大?
对于一种物品，要么装入背包，要么不装。
'''
# 01 背包问题
def knapsack01_v1(v, w, C):
    return process1(v, w, 0, C)


def process1(v, w, index, rest):
    if rest < 0: return -1
    if index == len(w): return 0
    p1 = process1(v, w, index + 1, rest)
    p2 = 0
    n = process1(v, w, index + 1, rest - w[index])
    if n != -1:
        p2 = v[index] + n
    return max(p1, p2)


def knapsack01_v2(v, w, C):
    return process2(v, w, 0, C)


def process2(v, w, index, rest):
    if index == len(w): return 0
    return max(process2(v, w, index + 1, rest),
               process2(v, w, index + 1, rest - w[index]) + v[index] if rest >= w[index] else 0)


def knapsack01_v3(v, w, C):
    n = len(w)
    dp = [[0] * (C + 1) for _ in range(n + 1)]

    for row in range(n - 1, -1, -1):
        for col in range(1, C + 1):
            dp[row][col] = max(dp[row + 1][col], dp[row + 1][col - w[row]] + v[row] if col >= w[row] else 0)

    return dp[0][C]


def knapsack01_v4(v, w, C):
    n = len(w)
    dp = [0] * (C + 1)

    for row in range(n - 1, -1, -1):
        for col in range(C, -1, -1):
            dp[col] = max(dp[col], dp[col - w[row]] + v[row] if col >= w[row] else 0)
    return dp[C]


def knapsack01_v5(v, w, C):
    n = len(w)
    dp = [0] * (C + 1)

    for row in range(n):
        for col in range(C, -1, -1):
            dp[col] = max(dp[col], dp[col - w[row]] + v[row] if col >= w[row] else 0)
    return dp[C]


import random


def generator_random_array(max_value, size):
    return [int(random.random() * max_value) + 1 for _ in range(size)]


def check():
    max_value = 10
    max_size = 10
    for i in range(500):
        size = int(random.random() * max_size)
        w = generator_random_array(max_value, size)
        c = int(random.random() * sum(w))

        v = generator_random_array(max_value, size)
        res1 = knapsack01_v1(w, v, c)
        res2 = knapsack01_v2(w, v, c)
        res3 = knapsack01_v3(w, v, c)
        res4 = knapsack01_v4(w, v, c)
        res5 = knapsack01_v5(w, v, c)

        if res1 != res2 or res1 != res3 or res1 != res4 or res1 != res5:
            print("ERROR", res1, res2, res3, res4, w, v, c)
    print("OVER!")


check()
