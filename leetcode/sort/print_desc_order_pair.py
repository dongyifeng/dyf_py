'''
在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有的逆序对。
'''


def get_desc_order_pair(nums):
    if not nums or len(nums) < 2: return []
    res = []
    process(nums, 0, len(nums) - 1, res)
    return res


def process(nums, l, r, res):
    if l == r: return
    mid = (l + r) >> 1

    process(nums, l, mid, res)
    process(nums, mid + 1, r, res)
    merge(nums, l, mid, r, res)


def merge(nums, l, mid, r, res):
    help = []
    p1 = l
    p2 = mid + 1

    while p1 <= mid and p2 <= r:
        if nums[p1] <= nums[p2]:
            help.append(nums[p1])
            p1 += 1
        else:
            for i in range(p1, mid + 1):
                res.append((nums[i], nums[p2]))
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


def get_desc_order_pair2(nums):
    if not nums or len(nums) < 2: return []
    res = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                res.append((nums[i], nums[j]))
    return res


import random


def random_array_generator(max_size, max_value):
    size = int(random.random() * max_size)
    return [int(random.random() * max_value) - int(random.random() * max_value) for _ in range(size)]


def check():
    n = 5000
    max_size = 10
    max_value = 10
    for i in range(n):
        nums = random_array_generator(max_size, max_value)
        nums2 = nums[:]
        expect = get_desc_order_pair2(nums2).sort()
        actual = get_desc_order_pair(nums).sort()

        if expect != actual:
            print("expect:", expect, "actual:", actual, "nums:", nums)
    print("Game Over!")


check()
