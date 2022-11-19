'''
给定一个字符串 str，返回把 str 全部切成回文子串的最小切割数。
【举例】
str = “ABA” 不需要切割，str 本身就是回文串，所以返回 0
str = “ACDCDCDAD” 最少需要切 2 次变成 3 个回文子串，比如“A”、“CDCDC” 和 “DAD”，所以返回 2.
'''

import sys


def min_cut(string):
    if not string: return 0
    return f(string, 0) - 1


def f(string, index):
    if index == len(string): return 0

    res = sys.maxsize
    for i in range(index, len(string)):
        if verify(string, index, i):
            num = f(string, i + 1) + 1
            res = min(res, f(string, i + 1) + 1)

    return res


def verify(string, i, j):
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def min_cut2(string):
    if not string: return 0
    dp = [0] * (len(string) + 1)
    for i in range(len(string) - 1, -1, -1):
        res = sys.maxsize
        for j in range(i, len(string)):
            if verify(string, i, j):
                res = min(res, dp[j + 1] + 1)
        dp[i] = res
    return dp[0] - 1


def min_cut3(string):
    if not string: return 0
    dp = [0] * (len(string) + 1)

    palindrome_dp = palindrome2(string)
    for i in range(len(string) - 1, -1, -1):
        res = sys.maxsize
        for j in range(i, len(string)):
            if palindrome_dp[i][j]:
                res = min(res, dp[j + 1] + 1)
        dp[i] = res
    return dp[0] - 1


def palindrome(string):
    n = len(string)
    dp = [[False] * n for _ in range(n)]
    # base case
    dp[-1][-1] = True
    for i in range(n - 1):
        dp[i][i] = True
        dp[i][i + 1] = string[i] == string[i + 1]

    for col in range(2, n):
        i = 0
        j = col
        while i < n - 2 and j < n:
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            i += 1
            j += 1
    return dp


def palindrome2(string):
    n = len(string)
    dp = [[False] * n for _ in range(n)]
    # base case
    dp[-1][-1] = True
    for i in range(n - 1):
        dp[i][i] = True
        dp[i][i + 1] = string[i] == string[i + 1]

    for row in range(n - 3, -1, -1):
        for col in range(row + 2, n):
            dp[row][col] = string[row] == string[col] and dp[row + 1][col - 1]

    return dp


import random


def generator_random_str(max_size):
    alphabet = [chr(i) for i in range(97, 123)]
    size = int(random.random() * max_size)
    return ''.join([random.sample(alphabet, 1)[0] for _ in range(size)])


def check():
    max_size = 10
    for i in range(500):
        stirng1 = generator_random_str(max_size)

        res1 = min_cut(stirng1)
        res2 = min_cut2(stirng1)
        res3 = min_cut3(stirng1)

        if res1 != res2 or res2 != res3:
            print("ERROR", stirng1, "res1=", res1, "res2=", res2, "res3=", res3)
    print("OVER")


# check()
def fun(x):
    return 1.0 / (1 + math.exp(-3*x))


import math

import matplotlib.pyplot as plt
import numpy as np

x = list(np.linspace(-2, 2, 500))  # -1到1中画50个点
# y=x**2
y = []
for data in x:
    y.append(fun(data))

y1 = x

print(y)

plt.margins(x=0)
plt.margins(y=0)

plt.plot(x, y, color='green')
plt.plot(x, y1, color='red')

plt.tick_params(axis='x', colors='blue')
plt.tick_params(axis='y', colors='red')
plt.show()

# print(palindrome("sifmumlkk"))
# min_split_count3("sifmumlkk")
