# coding=utf-8
'''
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    
    你可以假设数组中不存在重复的元素。
    
    你的算法时间复杂度必须是 O(log n) 级别。
    
    示例 1:
    
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
    示例 2:
    
    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1
    '''
import sys


def binary_search(nums, target):
    # print nums, target
    if not nums or nums[0] > target or nums[-1] < target: return -1
    start = 0
    end = len(nums)
    middle = (start + end) / 2
    while start <= middle <= end:
        if nums[middle] == target: return middle
        if nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) / 2
    return -1


import sys


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums: return -1
    rotation_index = len(nums)
    last = -sys.maxsize
    # 判断是否旋转
    for i in range(len(nums)):
        if nums[i] == target: return i
        if last > nums[i]:
            rotation_index = i
        last = nums[i]
    if rotation_index == len(nums) - 1: return -1

    left = nums[0: rotation_index]
    if left[-1] >= target >= left[0]:
        return binary_search(left, target)
    else:
        right = nums[rotation_index: len(nums)]
        r = binary_search(right, target)
        return min(r, rotation_index + r)


# print search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
#
# print search(nums=[1], target=0)

# print search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
# print search(nums=[1, 3], target=0)

# print(search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
#
# print(search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))


def binary_search2(nums, target):
    start = 0
    end = len(nums) - 1
    if len(nums) == 1: return 0 if nums[0] == target else -1
    while start <= end:
        middle = int((start + end) / 2)

        if nums[middle] == target: return middle
        # 左边有序
        if nums[0] <= nums[middle]:
            if nums[0] <= target and target <= nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        # 右边有序
        else:
            if nums[middle] <= target and target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1

    return -1


# print(binary_search2([4, 5, 6, 7, 0, 1, 2], 0))
# print(binary_search2([4, 5, 6, 7, 0, 1, 2], 3))
# print(binary_search2([1], 3))
# print(binary_search2([1, 3], 0))
print(binary_search2([1, 3], 3))
