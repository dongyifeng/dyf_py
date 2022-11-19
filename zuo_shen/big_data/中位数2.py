import heapq
import sys


def get_median_heap(heap, nums_freq, t, n):
    sum_value = 0
    last_num = None

    while heap:
        num = heapq.heappop(heap)
        sum_value += nums_freq[num]
        if sum_value > t:
            break
        last_num = num

    if last_num == None or n % 2 != 0: return num

    if sum_value - nums_freq[num] == t:
        return (num + last_num) / 2

    return num


def process(nums, y, heap_size):
    num_freq_map = {}

    heap = []
    for num in nums:
        if num >= y: continue

        if num in num_freq_map:
            num_freq_map[num] += 1
            continue

        if len(heap) < heap_size:
            heapq.heappush(heap, num)
            num_freq_map[num] = num_freq_map.get(num, 0) + 1
            continue

        if num > heap[0]:
            data = heapq.heapreplace(heap, num)
            num_freq_map.pop(data)
            num_freq_map[num] = 1

    return (num_freq_map, heap)


def get_median(nums, heap_size):
    if not nums: return 0
    n = len(nums)

    index = int(n / 2)
    y = sys.maxsize
    num_total = 0
    while True:
        num_freq_map, heap = process(nums, y, heap_size)
        y = heap[0]
        num_total += sum(num_freq_map.values())
        if n - num_total <= index:
            break

    t = index - (n - num_total)
    if t == 0:
        if n % 2 != 0:
            return heap[0]
        else:
            one = heap[0]
            num_freq_map, heap = process(nums, y, heap_size)
            two = 0
            while heap:
                two = heapq.heappop(heap)
            return (one + two) / 2

    return get_median_heap(heap, num_freq_map, t, n)
    # tmp = []
    # while heap:
    #     num = heapq.heappop(heap)
    #     tmp += [num] * num_freq_map[num]
    #
    # if n % 2 != 0:
    #     return tmp[t]
    # else:
    #     return (tmp[t] + tmp[t - 1]) / 2


def get_median2(nums):
    if not nums: return 0
    nums.sort()
    n = len(nums)
    index = n >> 1
    if n % 2 == 0:
        return (nums[index] + nums[index - 1]) / 2
    return nums[index]


import random


def random_array_generator(max_size, max_value):
    size = int(random.random() * max_size)
    return [int(random.random() * max_value) for _ in range(size)]


def test():
    n = 10000
    max_size = 100
    max_value = 100

    for i in range(n):
        array = []
        try:
            array = random_array_generator(max_size, max_value)
            expect = get_median2(array)
            actual = get_median(array, 3)
            if expect != actual:
                print("ERROR", "expect:", expect, "actual", actual, array)
        except Exception as err:
            print("ERROR", array, err)
    print("OVER!")


# test()

# nums = [0, 0, 1, 6]
# print(get_median(nums, 3), get_median2(nums))
#
nums = [1, 1, 2, 2, 2, 3, 3]
print(get_median(nums, 3), get_median2(nums))

# nums = ["a", "b", "c", "d"]
# nums_freq = {"a": 11, "b": 7, "c": 1, "d": 18}
# n = 38
# print(get_test(nums, nums_freq, n))


import operator


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


stu1 = Student(1, 9)
stu2 = Student(2, 8)
stu3 = Student(3, 7)

print(stu1 > stu2)

[stu1, stu2, stu3].sort()
