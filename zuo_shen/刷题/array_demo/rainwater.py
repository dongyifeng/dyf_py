'''
给定一个数组 arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水?

比如，arr=【3，1，2，5，2，4】，根据值画出的直方图就是容器形状，该容器可以装下 5 格水。

再比如：arr=【4，5，1，3，2】，该容器可以装下 2 格水。
'''


def get_water(arr):
    if not arr or len(arr) < 3: return 0
    n = len(arr)

    left_max_value = [0] * n
    right_max_value = [0] * n

    for i in range(n):
        left_max_value[i] = max(left_max_value[i - 1], arr[i])

    max_value = 0
    for i in range(n - 1, -1, -1):
        max_value = max(max_value, arr[i])
        right_max_value[i] = max_value

    res = 0
    for i in range(n):
        res += max(min(left_max_value[i], right_max_value[i]) - arr[i], 0)
    return res


def get_water2(arr):
    if not arr or len(arr) < 3: return 0
    n = len(arr)

    left_max_value = [0] * n
    right_max_value = [0] * (n + 1)

    for i in range(n):
        left_max_value[i] = max(left_max_value[i - 1], arr[i])
        right_max_value[n - 1 - i] = max(right_max_value[n - i], arr[n - 1 - i])

    res = 0
    for i in range(n):
        res += max(min(left_max_value[i], right_max_value[i]) - arr[i], 0)
    return res


def get_water3(arr):
    if not arr or len(arr) < 3: return 0
    n = len(arr)

    left = 1
    right = n - 2
    left_max_value = arr[0]
    right_max_value = arr[-1]

    res = 0
    while left <= right:
        if left_max_value < right_max_value:
            res += max(left_max_value - arr[left], 0)
            left_max_value = max(left_max_value, arr[left])
            left += 1
        else:
            res += max(right_max_value - arr[right], 0)
            right_max_value = max(right_max_value, arr[right])
            right -= 1

    return res


import random


def random_array_generator(max_value, max_size):
    return [int(random.random() * max_value + 1) for _ in range(int(random.random() * max_size))]


def check():
    n = 1000
    max_value = 100
    max_size = 100

    for _ in range(n):
        arr = random_array_generator(max_value, max_size)
        res1 = get_water(arr)
        res2 = get_water2(arr)
        res3 = get_water3(arr)

        if res1 != res2 or res1 != res3:
            print("Error", arr, res1, res2, res3)
    print("Game Over!")


check()
