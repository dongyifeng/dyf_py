'''
给定一个正数 1，裂开的方法有一种：(1)
给定一个正数 2，裂开的方法有一种：(1，1)，(2)
给定一个正数 3，裂开的方法有一种：(1，1，1)，(1，2)，(3)
给定一个正数 4，裂开的方法有一种：(1，1，1，1)，(1，1，2)，(1，3)，(2，2)，(4)
给定一个正数 n，求裂开的方法数。
'''


def ways(n):
    return f(1, n)


def f(pre, rest):
    if rest == 0: return 1
    if rest < pre: return 0
    res = 0
    for i in range(pre, rest + 1):
        res += f(i, rest - i)
    return res


def ways1(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][i] = 1

    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            res = 0
            for i in range(pre, rest + 1):
                res += dp[i][rest - i]
            dp[pre][rest] = res

    return dp[1][-1]


def ways2(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][i] = 1

    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            dp[pre][rest] = dp[pre][rest - pre] + dp[pre + 1][rest]

    return dp[1][-1]


import random


def check():
    max_value = 100
    for _ in range(1000):
        n = int(random.random()) * max_value + 1
        res = ways(n)
        res1 = ways1(n)
        res2 = ways2(n)

        if res != res1 or res != res2:
            print("ERROR", "res=", res, "res1=", res1, "res2=", res2, n)
    print("OVER")


check()

print(ways(1))
print(ways(2))
print(ways(3))
print(ways(4))

print("-" * 100)

print(ways2(1))
print(ways2(2))
print(ways2(3))
print(ways2(4))

print("-" * 100)

print(ways1(1))
print(ways1(2))
print(ways1(3))
print(ways1(4))
