def quick_sort(nums, low, high):
    if low >= high: return

    swap(nums, random.randint(low, high), high)

    m1, m2 = partition(nums, low, high)
    quick_sort(nums, low, m1 - 1)
    quick_sort(nums, m2 + 1, high)


def partition(nums, low, high):
    less = low - 1
    more = high

    while low < more:
        if nums[low] < nums[high]:
            less += 1
            swap(nums, less, low)
            low += 1
        elif nums[low] == nums[high]:
            low += 1
        else:
            more -= 1
            swap(nums, more, low)

    swap(nums, high, more)
    return less + 1, more


def quick_sort2(nums, low, high):
    if low >= high: return

    m1, m2 = partition2(nums, low, high)
    quick_sort2(nums, low, m1)
    quick_sort2(nums, m2, high)


def partition2(nums, low, high):
    less = low - 1
    more = high + 1
    x = nums[random.randint(low, high)]

    while low < more:
        if nums[low] < x:
            less += 1
            swap(nums, less, low)
            low += 1
        elif nums[low] == x:
            low += 1
        else:
            more -= 1
            swap(nums, more, low)

    return less, more


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


import random


def random_array_generator(max_size, max_value):
    size = int(random.random() * max_size)

    return [int(random.random() * max_value) - int(random.random() * max_value) for _ in range(size)]


def check():
    n = 10000
    max_size = 10
    max_value = 10

    for i in range(n):
        nums = random_array_generator(max_size, max_value)
        nums2 = nums[:]

        quick_sort2(nums, 0, len(nums) - 1)
        nums2.sort()

        if nums2 != nums:
            print("ERROR:nums", nums, "nums2", nums2)
    print("Game Over!")


check()


# nums = [3, 0, 3, 4, 2, 5, 5, 9, 6]
# quick_sort2(nums, 0, len(nums) - 1)
# print(nums)
