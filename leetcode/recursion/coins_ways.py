'''
arr 里都是正数，没有重复值，每一个值都代表一种货币，每一种货币都可以用无限张。最终要找零钱数是 aim，返回找零方法数？
'''


def ways(arr, aim):
    if not arr: return 0
    return process(arr, 0, aim)


def process(arr, cur, rest):
    if len(arr) == cur or rest < 0: return 1 if rest == 0 else 0

    i = 0
    ways = 0
    while rest >= i * arr[cur]:
        ways += process(arr, cur + 1, rest - (i * arr[cur]))
        i += 1
    return ways


def ways2(arr, aim):
    if not arr: return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for cur in range(n - 1, -1, -1):
        for rest in range(1, aim + 1):

            i = 0
            while rest >= i * arr[cur]:
                dp[cur][rest] += dp[cur + 1][rest - (i * arr[cur])]
                i += 1

    for row in dp:
        print(row)

    return dp[0][aim]


def ways3(arr, aim):
    if not arr: return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for cur in range(n - 1, -1, -1):
        for rest in range(1, aim + 1):
            dp[cur][rest] = dp[cur + 1][rest]
            dp[cur][rest] += dp[cur][rest - arr[cur]] if rest - arr[cur] >= 0 else 0

    for row in dp:
        print(row)

    return dp[0][aim]


import random


def random_array_generator(max_value, max_size):
    return [int(random.random() * max_value + 1) for _ in range(int(random.random() * max_size + 1))]


def check():
    n = 100
    max_value = 10
    max_size = 10

    for _ in range(n):
        arr = random_array_generator(max_value, max_size)
        aim = int(random.random() * sum(arr) + 1)
        res = ways(arr, aim)
        res2 = ways2(arr, aim)
        res3 = ways3(arr, aim)

        if res != res2 or res != res3:
            print("Error", arr, aim, res, res2, res3)
    print("Game Over!")


# check()
arr = [1, 2, 3, 4]
aim = 5

print(ways2(arr, aim))
print("-" * 100)
print(ways3(arr, aim))
