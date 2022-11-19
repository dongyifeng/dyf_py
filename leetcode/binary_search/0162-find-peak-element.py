# coding=utf-8
'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。
'''

import sys

'''
方案一：暴力求解
'''


def findPeakElement(nums):
    if not nums: return -1
    n = len(nums)
    nums.insert(0, -sys.maxint)
    nums.append(-sys.maxint)

    for i in range(1, n + 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i - 1
    return 0


'''
方案一：暴力求解
由于存在：nums[i] ≠ nums[i+1]，那么 if  nums[i] > nums[i + 1] ，则 i 是峰值
'''


def findPeakElement2(nums):
    if not nums: return -1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1


'''
在简单的二分查找中，我们处理的是一个有序数列，并通过在每一步减少搜索空间来找到所需要的数字。在本例中，我们对二分查找进行一点修改。首先从数组
nums 中找到中间的元素 mid。若该元素恰好位于降序序列或者一个局部下降坡度中（通过将 nums[i] 与右侧比较判断)，则说明峰值会在本元素的左边。于是，我们将搜索空间缩小为
mid 的左边(包括其本身)，并在左侧子数组上重复上述过程。
'''


def findPeakElement3(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        # mid 在下降
        if nums[mid] > nums[right]:
            right = mid
        # mid 在上升
        else:
            left = mid + 1
    return left


def find_peak_element4(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        # mid 在下降
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # mid 在上升
        else:
            right = mid
    print(left,mid,right)
    return left


print(find_peak_element4([1, 2]))
#
print(find_peak_element4([1, 2, 3, 1]))
#
print(find_peak_element4([1, 2, 1, 3, 5, 6, 4]))
print(find_peak_element4([1, 2, 1, 3, 5, 6, 7]))
