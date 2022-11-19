'''
求象棋中马从 （0,0） 点通过 k 步跳到 B 点 ，一共有多少走法？象棋棋盘是9行10列的矩阵
'''


def way(row, col, k):
    return process(row, col, k)


def process(row, col, k):
    if row > 8 or col > 9 or row < 0 or col < 0 or k < 0:
        return 0

    if k == 0 and row == 0 and col == 0:
        return 1

    return process(row - 1, col - 2, k - 1) + \
           process(row - 2, col - 1, k - 1) + \
           process(row - 2, col + 1, k - 1) + \
           process(row - 1, col + 2, k - 1) + \
           process(row + 1, col + 2, k - 1) + \
           process(row + 2, col + 1, k - 1) + \
           process(row + 2, col - 1, k - 1) + \
           process(row + 1, col + 2, k - 1)


def way2(x, y, rest):
    max_row = 9
    max_col = 10
    dp = [[[0] * max_col for _ in range(max_row)] for _ in range(rest + 1)]

    dp[0][0][0] = 1

    for k in range(1, rest + 1):
        for row in range(max_row):
            for col in range(max_col):
                dp[k][row][col] = get_value(dp, row - 1, col - 2, k - 1) + \
                                  get_value(dp, row - 2, col - 1, k - 1) + \
                                  get_value(dp, row - 2, col + 1, k - 1) + \
                                  get_value(dp, row - 1, col + 2, k - 1) + \
                                  get_value(dp, row + 1, col + 2, k - 1) + \
                                  get_value(dp, row + 2, col + 1, k - 1) + \
                                  get_value(dp, row + 2, col - 1, k - 1) + \
                                  get_value(dp, row + 1, col + 2, k - 1)

    return dp[rest][x][y]


def get_value(dp, row, col, k):
    if row > 8 or col > 9 or row < 0 or col < 0 or k < 0:
        return 0

    return dp[k][row][col]


import random


def check():
    n = 10
    max_row = 8
    max_col = 9

    for _ in range(n):
        row = int(random.random() * max_row + 1)
        col = int(random.random() * max_col + 1)
        k = int(random.random() * max_row + 1)

        if way(row, col, k) != way2(row, col, k):
            print("ERROR",row,col,k)
    print("Game Over!")

check()

# print(way2(5, 6, 7))
#
# print(way(5, 6, 7))
