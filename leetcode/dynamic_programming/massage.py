'''

一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

'''


def massage(nums):
    if not nums: return 0
    s1 = nums[0]
    s2 = max(nums[:2])
    res = max(s1, s2)
    for i in range(2, len(nums)):
        res = max(s1 + nums[i], s2)
        s1 = s2
        s2 = res

    return res


def massage2(nums):
    return process(nums, len(nums) - 1)


def process(nums, index):
    if index < 0: return 0
    if index == 0: return nums[0]
    if index == 1: return max(nums[0], nums[1])

    return max(nums[index] + process(nums, index - 2), process(nums, index - 1))


import random


def generator_random_array(max_value, max_size):
    return [int(random.random() * max_value) + 1 for _ in range(int(random.random() * max_size))]


def check():
    max_value = 20
    max_size = 20
    for i in range(50):
        arr = generator_random_array(max_value, max_size)
        res1 = massage(arr)
        res2 = massage2(arr)
        if res1 != res2:
            print("ERROR", res1, res2, arr)
    print("OVER!")


check()

print(massage([1, 2, 3, 1]))
print(massage([2, 7, 9, 3, 1]))
print(massage([2, 1, 4, 5, 3, 1, 1, 3]))
print(massage([2, 1, 1, 2]))

print("-" * 100)

print(massage2([1]))
print(massage2([1, 2]))

print(massage2([1, 2, 3, 1]))
print(massage2([2, 7, 9, 3, 1]))
print(massage2([2, 1, 4, 5, 3, 1, 1, 3]))
print(massage2([2, 1, 1, 2]))
