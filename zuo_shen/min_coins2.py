'''
给定数组 arr，arr 中所有的值都为正整数。每个值代表一张钱的面值，再给定一个整数 aim 代表要找的钱数，求组成 aim 的最少货币数。
'''

import sys


def min_coins(array, aim):
    return f(array, len(array) - 1, aim)


def f(array, i, rest):
    # base case
    # 钱不够或者硬币不够
    # 钱不够了
    if rest < 0: return -1
    # 上一步刚等于 aim，此时不需要硬币了
    if rest == 0: return 0
    # aim > 0 没有硬币可用了
    if i < 0:
        return -1

    # 不保留 arr[i]
    p1 = f(array, i - 1, rest)
    # 保留 arr[i]
    p2 = f(array, i - 1, rest - array[i])
    if p1 == -1 and p2 == -1:
        return -1
    elif p1 == -1 or p2 == -1:
        return max(p1, p2 + 1)
    return min(p1, p2 + 1)


def min_coins2(array, aim):
    if aim < 0 or not array: return -1
    if aim <= 0: return 0

    n = len(array)
    dp = [[sys.maxsize] * (aim + 1) for _ in range(n)]

    # base case
    if array[0] <= aim: dp[0][array[0]] = 1

    for i in range(1, n):
        for j in range(aim + 1):
            left_up = 1 if array[i] == j else sys.maxsize
            if j - array[i] >= 0 and dp[i - 1][j - array[i]] != sys.maxsize:
                left_up = dp[i - 1][j - array[i]] + 1
            dp[i][j] = min(left_up, dp[i - 1][j])

    # for row in dp:
    #     print(row)

    return dp[-1][-1] if dp[-1][-1] != sys.maxsize else -1


def min_coins3(array, aim):
    if aim < 0 or not array: return -1
    if aim <= 0: return 0

    n = len(array)
    dp = [sys.maxsize] * (aim + 1)

    # base case
    if array[0] <= aim: dp[array[0]] = 1

    for i in range(1, n):
        for j in range(aim, -1, -1):
            left_up = 1 if array[i] == j else sys.maxsize
            if j - array[i] >= 0 and dp[j - array[i]] != sys.maxsize:
                left_up = dp[j - array[i]] + 1
            dp[j] = min(left_up, dp[j])

    return dp[-1] if dp[-1] != sys.maxsize else -1


def print_matrix(m):
    for row in m:
        print(row)
    print("-" * 100)


def min_coins_count2(array, aim):
    return f2(array, aim, 0)


def f2(array, aim, cur):
    # 钱不够了
    if aim < 0: return -1
    # 上一步刚等于 aim，此时不需要硬币了
    if aim == 0: return 0
    # aim > 0 没有硬币可用了
    if cur == len(array):
        return -1

    # aim > 0 并且有硬币
    # 由于返回值有 -1，-1 会干扰求 min
    # min( f2(array, aim, cur + 1), f2(array, aim - array[cur], cur + 1))
    p1 = f2(array, aim, cur + 1)
    p2 = f2(array, aim - array[cur], cur + 1)

    if p1 == -1 and p2 == -1:
        return -1
    elif p1 == -1 or p2 == -1:
        return max(p1, p2 + 1)

    return min(p1, p2 + 1)


def min_coins_count3(array, aim):
    n = len(array)
    dp = [[-1] * (aim + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for cur in range(n - 1, -1, -1):
        for rest in range(1, aim + 1):
            p1 = dp[cur + 1][rest]
            p2 = dp[cur + 1][rest - array[cur]] if rest - array[cur] >= 0 else -1
            if p1 == -1 and p2 == -1:
                dp[cur][rest] = -1
            elif p1 == -1 or p2 == -1:
                dp[cur][rest] = max(p1, p2 + 1)
            else:
                dp[cur][rest] = min(p1, p2 + 1)

    return dp[0][aim]


import random


def generator_random_arr(max_size, max_value):
    return [int(random.random() * max_value) + 1 for _ in range(int(random.random() * max_size) + 1)]


def check():
    max_size = 10
    max_value = 10
    for _ in range(1000):
        arr = generator_random_arr(max_size, max_value)
        aim = int(random.random() * sum(arr)) + 1
        res = min_coins(arr, aim)
        res2 = min_coins2(arr, aim)
        res3 = min_coins3(arr, aim)
        res4 = min_coins_count2(arr, aim)
        res5 = min_coins_count3(arr, aim)
        if res != res2 or res != res3 or res != res4 or res != res5:
            print("ERROR", "res=", res, "res2=", res2, "res3=", res3, "res4=", res4, "res5=", res5, aim, arr)
    print("OVER")


check()
# print(min_coins2([2, 1], 1))
#
# print(min_coins2([10, 1, 4], 13))
# print("-"*100)
# print(min_coins3([1], 1))
