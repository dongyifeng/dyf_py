'''
给定数组 arr，arr 中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数 aim 代表要找的钱数，求换钱有多少种方法。

【例如】arr = [ 5, 10, 25, 1 ] , aim = 0 ；返回 1

组成 0 元的方法有 1 种，就是所有面值的货币都不用
'''


def process1(arr, index, aim):
    if index == len(arr):
        return 1 if aim == 0 else 0
    res = 0
    count = 0
    while arr[index] * count <= aim:
        res += process1(arr, index + 1, aim - arr[index] * count)
        count += 1
    return res


def coins1(arr, aim):
    if not arr or aim < 0:
        return 0
    return process1(arr, 0, aim)


def coins2(arr, aim):
    if not arr or aim < 0:
        return 0

    dp = [[0] * (aim + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    for i in range(1, aim + 1):
        if arr[0] * i < aim + 1:
            dp[0][arr[0] * i] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            count = 0
            while arr[i] * count <= j:
                dp[i][j] += dp[i - 1][j - arr[i] * count]
                count += 1

    return dp[len(arr) - 1][aim]


def coins3(arr, aim):
    if not arr or aim < 0:
        return 0

    dp = [[0] * (aim + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    for i in range(1, aim + 1):
        if arr[0] * i < aim + 1:
            dp[0][arr[0] * i] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - arr[i]] if (j - arr[i]) >= 0 else 0

    return dp[len(arr) - 1][aim]


print(coins1([3, 7, 5, 5, 10], 20))
print(coins2([3, 7, 5, 5, 10], 20))
print(coins3([3, 7, 5, 5, 10], 20))

print(coins1([5, 10, 25, 1], 15))
print(coins2([5, 10, 25, 1], 15))
print(coins3([5, 10, 25, 1], 15))

print('-' * 100)

# print(coins3([3, 7, 5, 5, 10], 20))

'''
给定数组 arr，arr 中所有的值都为正整数。每个值代表一种面值的货币，每种面值的货币只可使用一张，再给定一个整数 aim 代表要找的钱数，求换钱有多少种方法。
'''


def process4(arr, index, aim):
    if index == len(arr):
        return 1 if aim == 0 else 0

    return process4(arr, index + 1, aim - arr[index]) + process4(arr, index + 1, aim)


def coins4(arr, aim):
    if not arr or aim < 0:
        return 0
    return process4(arr, 0, aim)


def coins5(arr, aim):
    if not arr or aim < 0:
        return 0
    dp = [[0] * (aim + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1

    if arr[0] <= aim:
        dp[0][arr[0]] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i - 1][j - arr[i]] if j - arr[i] >= 0 else 0

    return dp[len(arr) - 1][aim]


# print(backage([2, 5, 10], 10))
print(coins4([3, 7, 5, 5, 10], 20))
print(coins5([3, 7, 5, 5, 10], 20))


def coins5(arr, aim):
    if not arr or aim < 0:
        return 0
    dp_1 = coins3(arr, aim)
    dp_2 = coins5(arr, aim)

    for i in range(len(arr)):
        for j in range(aim + 1):
            if dp_1[i][j] == 0: continue
            res += dp_1[i][j]
            for k in range(len(arr)):
                if dp_2[k][aim - j] >= 0 and aim - j >= 0:
                    res += dp_2[k][aim - j]
    return res
