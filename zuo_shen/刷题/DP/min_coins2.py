'''
给定数组 arr，arr 中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数 aim 代表要找的钱数，求组成 aim 的最少货币数。
'''

import sys

global map
map = {"1": 0, "2": 0}


def min_coins(arr, aim):
    return f(arr, aim, 0)


def f(arr, rest, i):
    global map
    map["1"] += 1
    if rest == 0: return 0
    if i == len(arr) or rest < 0: return -1

    count = 0
    res = sys.maxsize
    while count * arr[i] <= rest:
        p1 = f(arr, rest - count * arr[i], i + 1)
        if p1 != -1:
            res = min(res, p1 + count)
        count += 1

    return -1 if res == sys.maxsize else res


def min_coins_v1(arr, aim):
    arr.sort()
    return f_v1(arr, aim)


def f_v1(arr, rest):
    global map
    map["2"] += 1
    if map["2"] % 10000 == 0:
        print(map["2"],rest)
    if rest == 0: return 0

    res = sys.maxsize
    for coin in arr:
        if coin == rest:
            return 1
        if coin > rest:
            break
        num = f_v1(arr, rest - coin)
        if num != -1:
            res = min(res, num + 1)

    return res if res != sys.maxsize else -1


def min_coins2(arr, aim):
    if aim <= 0: return 0
    dp = [[-1] * (aim + 1) for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 0
    for j in range(aim + 1):
        dp[0][j] = int(j / arr[0]) if j % arr[0] == 0 else -1

    for i in range(1, len(arr)):
        for j in range(aim + 1):
            count = 0
            res = sys.maxsize
            while count * arr[i] <= j:
                p1 = dp[i - 1][j - count * arr[i]]
                if p1 != -1:
                    res = min(res, p1 + count)
                count += 1
                print("deploy", i - 1, j - count * arr[i])
            dp[i][j] = res
            print(i, j, "-" * 100)

    return dp[-1][aim]


def min_coins3(arr, aim):
    if aim <= 0: return 0
    dp = [[-1] * (aim + 1) for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 0

    for j in range(aim + 1):
        dp[0][j] = int(j / arr[0]) if j % arr[0] == 0 else -1

    for i in range(1, len(arr)):
        for j in range(aim + 1):

            # dp[i][j] = dp[i-1][j]+dp[]
            count = 0
            res = sys.maxsize
            while count * arr[i] <= j:
                p1 = dp[i - 1][j - count * arr[i]]
                if p1 != -1:
                    res = min(res, p1 + count)
                count += 1
            dp[i][j] = res

    return dp[-1][aim]


def min_coins4(array, aim):
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


import random


def generator_random_arr(max_size, max_value):
    return [item for item in
            set([int(random.random() * max_value) + 1 for _ in range(int(random.random() * max_size) + 1)])]


def check():
    global map
    max_size = 10
    max_value = 10
    for _ in range(100):
        arr = generator_random_arr(max_size, max_value)
        aim = int(random.random() * sum(arr)) + 1
        print("info2", aim, arr)
        res = min_coins(arr, aim)
        res2 = min_coins_v1(arr, aim)
        # print("Info", "res=", res, "res2=", res2, aim, arr)
        if res != res2 or res != res2:
            print("ERROR", "res=", res, "res2=", res2, aim, arr)
    print("OVER")

    print(map)


# check()

print(min_coins([1,4,   10], 44))
# print(min_coins2([3, 2, 5], 20))
print(min_coins_v1([1,4,   10], 44))
