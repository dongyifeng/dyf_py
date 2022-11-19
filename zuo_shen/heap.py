'''
已知一个几乎有序的数组。几乎有序是指，如果把数组排好顺序的话，每个元素移动的距离一定不超过 k，并且 k 相对于数组的长度来说比较小。
请选择一个合适的排序策略，对这个数组进行排序。
'''

import heapq
import sys


def sort(nums, k):
    data = []

    for i in range(len(nums)):
        if i < k:
            heapq.heappush(data, nums[i])
        else:
            nums[i - k] = heapq.heappop(data)
            heapq.heappush(data, nums[i])

    i = 0 if len(nums) < k else len(nums) - k
    while data:
        nums[i] = heapq.heappop(data)
        i += 1
    return nums


nums = [1, 2, 3, 6, 5]
sort(nums, k=3)
print(nums)

'''
> 给定很多线段，每个线段都有两个数组【start，end】，表示线段开始位置和结束位置，左右都是闭区间
> 规定：
> 1. 线段的开始和结束位置一定都是整数值
> 2. 线段重合区域的长度必须 >= 1
> 返回线段最多重合区域中，包含了几条线段。
'''


def segment_count(nums, x):
    res = 0
    for s, e in nums:
        if x > s and x < e:
            res += 1
    return res


def max_cover(nums):
    # 最小起点
    min_s = sys.maxsize
    # 最小终点
    max_e = 0
    for s, e in nums:
        min_s = min(min_s, s)
        max_e = max(max_e, e)

    x = min_s + 0.5
    res = 0
    while x < max_e:
        res = max(res, segment_count(nums, x))
        x += 0.5
    return res


print(max_cover([(1, 3), (2, 6), (4, 5), (3, 9)]))


def max_cover2(nums):
    nums.sort()

    heap = []
    res = 0
    for s, e in nums:
        if heap and s > heap[0]:
            heapq.heappop(heap)
        else:
            heapq.heappush(heap, e)
            res = max(res, len(heap))
    return res


print(max_cover2([(1, 3), (2, 6), (4, 5), (3, 9)]))

'''
设计 RandomPool 结构

设计一种结构，在该结构中有如下三种功能：

Insert(key)：将某个 key 加入到该结构中，做到不重复加入。

Delete(key)：将原本在结构中的某个 key 移除

getRandom()：等概率随机返回结构中任何一个 key。

【要求】：Insert、delete 和 getRandom 方法的时间复杂度都是 O(1)  '''

import random


class RandomPool:
    def __init__(self):
        self.data = {}
        self.reverse = {}

    def insert(self, key):
        if key in self.data: return
        size = len(self.data)
        self.data[key] = size
        self.reverse[size] = key

    def delete(self, key):
        if key not in self.data: return
        index = self.data[key]

        size = len(self.data) - 1
        last_key = self.reverse[size]
        self.reverse[index] = last_key
        self.data[last_key] = index

        self.data.pop(key)
        self.reverse.pop(size)

    def get_random(self):
        index = int(random.random() * (len(self.data)))
        return self.reverse[index]


random_pool = RandomPool()

random_pool.insert("a")
random_pool.insert("b")
random_pool.insert("c")
random_pool.insert("d")
random_pool.insert("e")

res = {}
for i in range(100):
    key = random_pool.get_random()
    res[key] = res.get(key, 0) + 1
print(res)
