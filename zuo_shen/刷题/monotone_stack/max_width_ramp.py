'''
给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
找出 A 中的坡的最大宽度，如果不存在，返回 0 。
'''


def max_width_ramp(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] >= arr[i]:
                res = max(res, j - i)
    return res


def max_width_ramp1(arr):
    stack = [0]
    for i in range(1, len(arr)):
        if arr[i] < arr[stack[-1]]:
            stack.append(i)

    i = len(arr) - 1
    res = 0
    while stack:
        if arr[stack[-1]] <= arr[i]:
            res = max(res, i - stack[-1])
            stack.pop()
        else:
            i -= 1

    return res


import random


def check():
    for _ in range(1000):
        arr = [int(random.random() * 100) + 1 for _ in range(int(random.random()*100) + 1)]
        res1 = max_width_ramp1(arr)
        res2 = max_width_ramp1(arr)
        print("Info",  res1, res2)
        if res1 != res2:
            print("ERROR", arr, res1, res2)
    print("OVER")

check()
# print(max_width_ramp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
# print(max_width_ramp1([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
