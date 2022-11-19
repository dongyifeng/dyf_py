'''
给定两个一维 int 数组 A 和 B，其中：A 是长度为 m、元素从小到大排好序的数组。B 是长度为 n、元素从小到大排好序的有序数组。
希望从 A 和 B 数组只中，找到第 K 小的数，要求：使用尽量少的比较次数。
【举例】
arr1 = [ 1, 2, 3, 4, 5 ] ， arr2 = [ 3, 4, 5 ] ，k = 1
1 是所有数据中第 1 小的数，所以返回 1
arr1 = [ 1, 2, 3 ] ， arr2 = [ 3, 4, 5, 6 ] ，k = 4
3 是所有数据中第 4 小的数，所以返回 3
【要求】
如果 arr1 的长度是 N，arr2 的长度为 M，时间复杂度度请达到 O（ log ( min {M ,N } ) ）,额外空间复杂度为 O(1)
'''

# 双指针
# 时间复杂度：O(K)
# 空间复杂度：O(1)

import sys


def find_kth_num(arr1, arr2, k):
    index1 = 0
    index2 = 0
    res = 0

    arr1.append(sys.maxsize)
    arr2.append(sys.maxsize)

    while index1 + index2 < k:
        if arr1[index1] < arr2[index2]:
            res = arr1[index1]
            index1 += 1
        else:
            res = arr2[index2]
            index2 += 1
    return res


def find_kth_num2(arr1, arr2, k):
    res = process(arr1, arr2, k, 0, len(arr1) - 1)
    if res >= 0:
        return arr1[res]
    res = process(arr2, arr1, k, 0, len(arr2) - 1)
    return arr2[res]


def process(arr1, arr2, k, left, right):
    if left > right:
        return -1
    mid = int((left + right) / 2)
    index = find(arr2, arr1[mid], 0, len(arr2) - 1) + 1

    if index + mid + 1 == k:
        return mid

    if arr1[mid] == arr2[index - 1] and index + mid == k:
        return mid

    if index + mid + 1 > k:
        return process(arr1, arr2, k, left, mid - 1)
    else:
        return process(arr1, arr2, k, mid + 1, right)


def find(arr1, k, left, right):
    if left > right:
        return right
    mid = int((left + right) / 2)
    if k == arr1[mid]: return mid

    if k > arr1[mid]: return find(arr1, k, mid + 1, right)
    return find(arr1, k, 0, mid - 1)


import random


def generator(size, max_value):
    return [int(random.random() * max_value) + 1 for _ in range(size)]


def check():
    max_value = 10
    max_size = 10
    n = 1000

    for i in range(n):
        size = int(random.random() * max_size) + 1
        arr1 = sorted(generator(size, max_value))
        arr2 = sorted(generator(size, max_value))

        k = int(random.random() * (len(arr1) + len(arr2)))
        while k == 0:
            k = int(random.random() * (len(arr1) + len(arr2)))

        expect = find_kth_num(arr1[:], arr2[:], k)
        actual = find_kth_num2(arr1[:], arr2[:], k)
        if expect != actual:
            print("ERROR", arr2, arr1, k, actual, expect)
    print("Over!")


# check()

# print(find_kth_num([1, 2, 3, 4, 5], [3, 4, 5], 1))
# print(find_kth_num([1, 2, 3], [3, 4, 5, 6], 4))

# arr = [1, 2, 4, 5, 6, 7]
# print(find(arr, 3, 0, len(arr) - 1))


# arr1 = [1, 3, 4, 6, 6]
# arr2 = [3, 4, 5, 6, 9]
# k = 4
# print(find_kth_num(arr1[:], arr2[:], k))
# print('-' * 100)
# print(find_kth_num2(arr1[:], arr2[:], k))

arr1 = [2, 2, 3]
arr2 = [1, 2, 2, 2, 7, 8, 9, 10]
k = 2

# print(find_kth_num(arr1[:], arr2[:], k))
# print('-' * 100)
print(find_kth_num2(arr1[:], arr2[:], k))

# print(find_kth_num2([1, 2, 3, 4, 5], [3, 4, 5], 1))
# print(find_kth_num2([1, 2, 3], [3, 4, 5, 6], 4))
# print(process([3, 4, 5, 6], [1, 2, 3], 3, 0, 3))
