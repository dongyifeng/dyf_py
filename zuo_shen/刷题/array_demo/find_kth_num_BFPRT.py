'''
在一个无序数组中，求最小的第 k 个数。
'''


def find_kth_num(arr, k):
    if not arr: return

    arr.sort()
    return arr[k - 1]


def find_kth_num2(arr, k):
    if not arr: return
    return process2(arr, k - 1, 0, len(arr) - 1)


def process2(arr, k, left, right):
    if left == right:
        return arr[left]
    x = median_of_medians(arr, left, right)
    less, more = partition(arr, x, left, right)
    if less < k < more:
        return arr[less + 1]

    if less >= k:
        return process2(arr, k, left, less)
    return process2(arr, k, more, right)


def partition(nums, x, low, high):
    less = low - 1
    more = high + 1

    while low < more:
        if nums[low] < x:
            less += 1
            nums[less], nums[low] = nums[low], nums[less]
            low += 1
        elif nums[low] == x:
            low += 1
        else:
            more -= 1
            nums[more], nums[low] = nums[low], nums[more]

    return less, more


def median_of_medians(arr, left, right):
    num = right - left + 1
    offset = 0 if num % 5 == 0 else 1
    # 分组
    m_arr = [0] * (int(num / 5) + offset)
    for i in range(len(m_arr)):
        left_i = left + i * 5
        right_i = left_i + 4
        m_arr[i] = get_median(arr, left_i, min(right_i, right))
    return process2(m_arr, int(len(m_arr) / 2), 0, len(m_arr) - 1)


def get_median(arr, left, right):
    insertion_sort(arr, left, right)
    sum = right + left
    # 获取上中位数
    mid = int((sum / 2) + (sum % 2))
    return arr[mid]


# 插入排序：获取中位数需要有序
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):
            if arr[j - 1] <= arr[j]: break
            arr[j - 1], arr[j] = arr[j], arr[j - 1]


import random


def generator_random_array(max_size, max_value):
    return [int(random.random() * max_value) - int(random.random() * max_value) for _ in
            range(int(random.random() * max_size))]


def check():
    max_size = 5
    max_value = 5
    for _ in range(10000):
        arr = generator_random_array(max_size, max_value)
        k = int(random.random() * (len(arr) - 2)) + 1

        res = find_kth_num(arr[:], k)
        res2 = find_kth_num2(arr[:], k)
        if res != res2:
            print("ERROR", arr, "k", k, "res=", res, "res2=", res2)
    print("OVER")


check()
#
arr = [0, -1, 4, 1]
print(find_kth_num2(arr, 2))
