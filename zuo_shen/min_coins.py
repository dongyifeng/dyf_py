# 换钱的最少货币
'''
给定数组 arr，arr 中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数 aim 代表要找的钱数，求组成 aim 的最少货币数。
'''

import sys


def min_coins(array, aim):
    return f(array, aim)


def f(array, rest):
    if rest <= 0: return 0

    res = sys.maxsize
    for coin in array:
        if rest == coin:
            return 1
        if coin < rest:
            continue

        num = f(array, rest - coin) + 1
        if num != -1:
            res = min(res, num)
    return -1 if res == sys.maxsize else res


def min_coins1(array, aim):
    if aim <= 0: return 0
    dp = [-1] * (aim + 1)

    for i in range(aim + 1):
        res = sys.maxsize
        for coin in array:

            if i == coin:
                res = 1
                break
            if i < coin or dp[i - coin] == -1:
                continue

            res = min(res, dp[i - coin] + 1)

        if res != sys.maxsize:
            dp[i] = res

    return dp[-1]


def min_coins2(array, aim):
    if aim <= 0: return 0
    array.sort()
    dp = [-1] * (aim + 1)

    for i in range(aim + 1):
        res = sys.maxsize
        for coin in array:
            if i < coin: break

            if i == coin:
                res = 1
                break
            if dp[i - coin] != -1:
                res = min(res, dp[i - coin] + 1)

        if res != sys.maxsize:
            dp[i] = res

    return dp[-1]





print(min_coins_count2([5, 2, 3], 20))
print(min_coins1([5, 2, 3], 20))
print(min_coins2([5, 2, 3], 20))
