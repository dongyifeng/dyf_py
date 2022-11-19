'''
给定两个有序数组 arr1 和 arr2 ，已知两个数组的长度都为 N，求两个数组中所有数的上中位数。

【举例】
arr1 = [ 1, 2, 3, 4 ] ， arr2 = [ 3, 4, 5, 6 ]
总共有 8 个数，那么上中位数是第 4 小的数，所以返回 3


arr1 = [ 0, 2, 3 ] ， arr2 = [ 3, 4, 5]
总共有 6 个数，那么上中位数是第 3 小的数，所以返回 2
【要求】
时间复杂度为 O( log N )，额外空间复杂度 O(1)
'''


def get_up_median(arr1, arr2):
    if not arr1 or not arr2 or len(arr1) != len(arr2): return
    return process(arr1, 0, len(arr1) - 1, arr2, 0, len(arr2) - 1)


def process(arr1, left1, right1, arr2, left2, right2):
    if left1 == right1 and left2 == right2:
        return min(arr1[left1], arr2[left2])

    mid1 = int((right1 - left1) / 2) + left1
    mid2 = int((right2 - left2) / 2) + left2
    if arr1[mid1] == arr2[mid2]: return arr1[mid1]
    # 数组长度为偶数
    if (right1 - left1) % 2 == 1 and (right2 - left2) % 2 == 1:
        if arr1[mid1] > arr2[mid2]:
            return process(arr1, left1, mid1, arr2, mid2 + 1, right2)
        else:
            return process(arr1, mid1 + 1, right1, arr2, left2, mid2)
    # 奇数
    else:
        if arr1[mid1] > arr2[mid2]:
            if arr1[mid1 - 1] < arr2[mid2]: return arr2[mid2]
            return process(arr1, left1, max(mid1 - 1, 0), arr2, mid2 + 1, right2)
        else:
            if arr2[mid2 - 1] < arr1[mid1]: return arr1[mid1]
            return process(arr1, mid1 + 1, right1, arr2, left2, max(mid2 - 1, 0))


def get_up_median2(arr1, arr2):
    if not arr1 or not arr2 or len(arr1) != len(arr2): return

    data = []

    for item in arr1:
        data.append(item)

    for item in arr2:
        data.append(item)
    mid = int(len(data) / 2) - 1
    data = sorted(data)
    return data[mid]


def get_up_median3(arr1, arr2):
    if not arr1 or not arr2 or len(arr1) != len(arr2): return

    left1 = left2 = 0
    right1 = right2 = len(arr1) - 1
    while left1 < right1:
        mid1 = int((left1 + right1) / 2)
        mid2 = int((left2 + right2) / 2)

        if arr1[mid1] == arr2[mid2]:
            return arr1[mid1]

        # 元素个数为奇数，offset = 0；元素个数为偶数：offset = 1
        offset = 1 if (right1 - left1) % 2 == 1 else 0
        if arr1[mid1] > arr2[mid2]:
            right1 = mid1
            left2 = mid2 + offset
        else:
            left1 = mid1 + offset
            right2 = mid2

    return min(arr1[left1], arr2[left2])


import random


def generator(size, max_value):
    return [int(random.random() * max_value) + 1 for _ in range(size)]


def check():
    max_value = 10
    max_size = 10
    n = 100

    for i in range(n):
        size = int(random.random() * max_size) + 1
        arr1 = sorted(generator(size, max_value))
        arr2 = sorted(generator(size, max_value))
        expect = get_up_median(arr1[:], arr2[:])
        actual = get_up_median2(arr1[:], arr2[:])
        actual2 = get_up_median3(arr1[:], arr2[:])
        if expect != actual or expect != actual2:
            print("ERROR", arr2, arr1, actual, actual2, expect)
    print("Over!")


# check()
arr1 = [5, 6]
arr2 = [3, 9]

print(get_up_median3(arr1, arr2))
