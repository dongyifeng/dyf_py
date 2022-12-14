'''
给定一个数组 arr，该数组无序，但每个值均为正整数，再给定一个正数 k，求 arr 的所有子数组中所有元素相加和为 k 的最长子数组长度。
【例如】 arr = 【1,2,1,1,1】，k = 3
累加和为 3 的最长子数组为 [ 1, 1, 1 ]，所以结果返回 3.
要求：时间复杂度 O( N )，额外空间复杂度：O( 1 )
'''


def max_len_sub_list(arr, k):
    left = 0
    right = 0
    sub_sum = arr[0]
    res = 0
    while right < len(arr) and left<len(arr):
        if sub_sum == k:
            res = max(res, right - left + 1)
            sub_sum -= arr[left]
            left += 1

        elif sub_sum < k:
            right += 1
            if right == len(arr): break
            sub_sum += arr[right]
        else:
            sub_sum -= arr[left]
            left += 1

    return res


def max_len_sub_list2(arr, k):
    res = 0
    n = len(arr)
    for i in range(n):
        sub_sum = 0
        for j in range(i, n):
            sub_sum += arr[j]
            if sub_sum >= k: break

        if sub_sum == k:
            res = max(res, j - i + 1)
            # print("max_len_sub_list2", i, j, sub_sum)

    return res


import random


def generator_random_array(max_value, max_size):
    return [int(random.random() * max_value + 1) for _ in range(int(random.random() * max_size + 1))]


def check():
    max_value = 10
    max_size = 10

    for i in range(100):
        arr1 = generator_random_array(max_value, max_size)

        k = int(random.random() * sum(arr1))

        actual = max_len_sub_list(arr1, k)
        expect = max_len_sub_list2(arr1, k)
        if expect != actual:
            print("ERROR", expect, actual, arr1, k)


# arr1 = [6, 1, 2, 9, 4, 5]
# k = 3
# #
# print(max_len_sub_list(arr1, k))
# print(max_len_sub_list2(arr1, k))

check()
