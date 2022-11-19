'''
给定一个整型矩阵，返回子矩阵的最大累计和。
'''

import sys


# 返回子矩阵的最大累计和
def sub_matrix_max_sum(M):
    res = -sys.maxsize
    for i in range(len(M)):
        res = max(sub_array_max_sum(M[i]), res)

        if i == len(M) - 1: break
        for j in range(len(M[0])):
            M[i + 1][j] += M[i][j]
    return res


# 返回子数组中最大累计和
def sub_array_max_sum(a):
    cur = 0
    res = -sys.maxsize
    for item in a:
        cur += item
        res = max(res, cur)
        cur = max(0, cur)

    return res


print(sub_array_max_sum([-7, 9, -5, 3]))

print(sub_matrix_max_sum([[-5, 3, 6, 4], [-7, 9, -5, 3], [-10, 1, -200, 4]]))
