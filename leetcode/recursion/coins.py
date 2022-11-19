'''
给一个正整数数组 arr=【2,7,3，5,3】，每一个数表示一枚硬币，硬币可以重复。再一个 aim=10，求用硬币组成 aim，有多少种硬币的组合数？
'''


def coins(array, aim):
    return f(array, aim, 0, 0)


def f(array, aim, cur, s):
    if cur == len(array):
        return 1 if s == aim else 0

    return f(array, aim, cur + 1, s) + f(array, aim, cur + 1, s + array[cur])


def coins2(array, aim):
    n = len(array)
    dp = [[0] * (aim + 1) for _ in range(n + 1)]

    dp[-1][-1] = 1

    for row in dp:
        print(row)

    for cur in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[cur][rest] = dp[cur + 1][rest] + (0 if rest + array[cur] > aim else dp[cur + 1][rest + array[cur]])

    print('-' * 100)
    for row in dp:
        print(row)

    return dp[0][0]


import random


def random_array_generator(max_value, max_size):
    return [int(random.random() * max_value + 1) for _ in range(int(random.random() * max_size + 1))]


def check():
    n = 100
    max_value = 10
    max_size = 10

    for i in range(n):
        array = random_array_generator(max_size, max_value)
        aim = int(random.random() * sum(array))
        if coins(array, aim) != coins2(array, aim):
            print("ERROR", aim, array, coins(array, aim), coins2(array, aim))
    print("Game Over!")


#
array = [2, 4, 3, 1]
aim = 5
print(coins2(array, aim))
# print(coins(array, aim))
# check()
