# 375. 猜数字大小 II
import sys


def get_money_amount(n):
    dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            tmp = 0
            dp[i][j] = (i, j)

    for line in dp:
        print(line)


def binary_search(n, target):
    left = 0
    right = n
    amount = 0
    while left <= right:
        mid = (left + right) >> 1
        if target == mid: return amount
        amount += mid
        if mid > target:
            right = mid - 1
        else:
            left = mid + 1


print(get_money_amount(10))
