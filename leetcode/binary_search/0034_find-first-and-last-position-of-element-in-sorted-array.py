# coding=utf-8
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''


def searchRange(nums, target):
    if not nums or nums[0] > target or nums[-1] < target: return [-1, -1]
    start = 0
    end = len(nums)
    mid = end >> 1
    f = False
    while start <= mid <= end:
        if nums[mid] == target:
            f = True
            break
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) >> 1
    if not f: return [-1, -1]

    i = j = mid

    while i >= 0:
        if nums[i] == target:
            i -= 1
        else:
            break
    while j < len(nums):
        if nums[j] == target:
            j += 1
        else:
            break
    return [i + 1, j - 1]


def binary_search(nums, target):
    if not nums or nums[0] > target or nums[-1] < target: return -1
    start = 0
    end = len(nums)
    middle = int((start + end) / 2)
    while start <= middle <= end:
        if nums[middle] == target: return middle
        if nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
        middle = int((start + end) / 2)
    return -1


def search_range(nums, target):
    pos = binary_search(nums, target)
    if pos == -1: return [pos, pos]

    s = pos - 1
    while s >= 0:
        if nums[s] == target:
            s -= 1
        else:
            break

    e = pos + 1
    while e < len(nums):
        if nums[e] == target:
            e += 1
        else:
            break
    return [s + 1, e - 1]



print(search_range([2, 2], 2))
print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([1, 2], 1))
