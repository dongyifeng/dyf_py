'''
在一个无序数组中，求最小的第 k 个数。
'''


def find_kth_num(arr, k):
    if not arr: return

    arr.sort()
    return arr[k - 1]


import heapq


def find_kth_num2(arr, k):
    if not arr: return
    # 大顶锥
    heap = [-item for item in arr[:k]]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if -heap[0] > arr[i]:
            heapq.heappushpop(heap,-arr[i])
    return -heap[0]


def find_kth_num1(arr, k):
    if not arr: return
    return process(arr, k - 1, 0, len(arr) - 1)


def process(arr, k, left, right):
    index = random_range(left, right + 1)
    less, more = partition(arr, index, left, right)
    if less < k < more:
        return arr[less + 1]

    if less >= k:
        return process(arr, k, left, less)
    return process(arr, k, more, right)


def partition(nums, index, low, high):
    less = low - 1
    more = high + 1
    x = nums[index]

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


def random_range(left, right):
    return int(random.random() * (right - left)) + left





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
        # print(arr, k)

        res = find_kth_num(arr[:], k)
        res1 = find_kth_num1(arr[:], k)
        res2 = find_kth_num2(arr[:], k)
        if res != res1 or res != res2:
            print("ERROR", arr, "k", k, "res=", res, "res1=", res1, "res2=", res2)
    print("OVER")


check()
#
# arr = [0, -1, 2, 1]
# print(find_kth_num2(arr, 1))
# print(find_kth_num4(arr, 2))
