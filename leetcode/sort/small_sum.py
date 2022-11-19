'''
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。

【例子】【1	3	4	2	5】

1 左边比 1 的小的数，没有；

3 左边比 3 的小的数，1；

4 左边比 4 的小的数，1、3；

2 左边比 2 的小的数，1；

5 左边比 5 的小的数，1、3、4、2；

所以小和为：1 + 1 +3 + 1 + 1 + 3 + 4 +2 = 16

'''


def small_sum(nums):
    if not nums or len(nums) < 2: return 0

    return process(nums, 0, len(nums) - 1)


# num[l..r] 纪要排好，也要求小和
def process(nums, l, r):
    if l == r: return 0

    mid = (l + r) >> 1
    return process(nums, l, mid) + process(nums, mid + 1, r) + merge(nums, l, mid, r)


def merge(nums, l, mid, r):
    help = []
    p1 = l
    p2 = mid + 1
    res = 0
    while p1 <= mid and p2 <= r:
        if nums[p1] < nums[p2]:
            res += (r - p2 + 1) * nums[p1]
            help.append(nums[p1])
            p1 += 1
        else:
            help.append(nums[p2])
            p2 += 1

    while p1 <= mid:
        help.append(nums[p1])
        p1 += 1

    while p2 <= r:
        help.append(nums[p2])
        p2 += 1

    for i in range(len(help)):
        nums[l + i] = help[i]
    return res


def small_sum2(nums):
    if not nums or len(nums) < 2: return 0
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                res += nums[i]
    return res


import random


def random_array_generator(max_size, max_value):
    size = int(random.random() * max_size)
    return [int(random.random() * max_value) - int(random.random() * max_value) for _ in range(size)]


def check():
    n = 5000
    max_size = 100
    max_value = 100

    for i in range(n):
        nums = random_array_generator(max_size, max_value)
        nums2 = nums[:]
        expect = small_sum2(nums2)
        actual = small_sum(nums)
        if expect != actual:
            print("expect", expect, "actual", actual, "nums:", nums)
            break
    print("game Over!")


check()
