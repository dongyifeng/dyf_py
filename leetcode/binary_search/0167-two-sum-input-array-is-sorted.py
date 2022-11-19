# coding=utf-8
'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''

'''
二分查找
'''


def search(i, nums, target):
    if len(nums) <= i or nums[i] > target or nums[-1] < target: return -1
    l = i
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target: return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


'''
去掉nums[i]，在 i 后边的数组中查找 target - nums[i]
'''


def two_sum(numbers, target):
    n = len(numbers) - 1
    for i in range(n):
        r = search(i + 1, numbers, target - numbers[i])
        if r > 0: return (i + 1, r + 1)
    return (-1, -1)


# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([2, 3, 4], 6))
# print(two_sum([3, 24, 50, 79, 88, 150, 345], 200))
print(two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8))


def two_sum2(numbers, target):
    high = len(numbers) - 1
    low = 0
    while low < high:
        tmp = numbers[low] + numbers[high]
        if tmp == target: return (low + 1, high + 1)
        if tmp > target:
            high -= 1
        else:
            low += 1

    return (-1, -1)


print(two_sum2([2, 7, 11, 15], 9))
print(two_sum2([2, 3, 4], 6))
print(two_sum2([3, 24, 50, 79, 88, 150, 345], 200))
print(two_sum2([1, 2, 3, 4, 4, 9, 56, 90], 8))
