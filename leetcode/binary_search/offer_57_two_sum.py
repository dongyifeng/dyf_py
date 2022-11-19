'''
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
'''


def two_sum(nums, target):
    for i in range(len(nums)):
        p = find(nums, target - nums[i], i)
        if p != -1:
            return [nums[i], nums[p]]
    return []


def find(nums, target, left):
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def two_sum2(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        tmp = nums[left] + nums[right]
        if tmp == target:
            return [nums[left], nums[right]]
        if tmp < target:
            left += 1
        else:
            right -= 1
    return []


print(two_sum2([2, 7, 11, 15], 9))
print(two_sum2([10, 26, 30, 31, 47, 60], 40))
print(two_sum2([14, 15, 16, 22, 53, 60], 76))
