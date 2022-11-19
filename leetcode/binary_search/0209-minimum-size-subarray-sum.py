# coding=utf-8
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''

'''
暴力
'''


def minSubArrayLen(target, nums):
    start = 0
    n = len(nums)
    end = n
    f = False
    for i in range(n):
        s = nums[i]
        for j in range(i + 1, n + 1):
            if s >= target:
                f = True
                if (end - start) > (j - i):
                    start = i
                    end = j
                break
            if j < n: s += nums[j]
    return end - start if f else 0


# print minSubArrayLen(7, [2, 3, 1, 2, 4, 3])

# print minSubArrayLen(4, [1, 4, 4])
#
# print minSubArrayLen(11, [1, 2, 3, 4, 5])

import sys

'''
算法优化：查看有哪些步骤，是重复运算，能否设计一个结构，将结果保存，下次只计算改变的部分，而非重新计算。

本地优化关键点：连续和 = s
设置一个窗口：
    当 s < target 时，窗口左边不变，右边向前延伸。
    当 s >= target 时，获取截止到现在，最小窗口，然后窗口右边不变，左边开始收缩，已探测窗口是否可以更小。
'''


def minSubArrayLen2(target, nums):
    res = sys.maxsize
    left = 0
    right = -1
    s = 0
    n = len(nums)
    while right < len(nums) and left < len(nums):
        if s < target and right == n - 1: break
        if s < target:
            right += 1
            s += nums[right]
        if s >= target:
            res = min(right - left + 1, res)
            s -= nums[left]
            left += 1
    return 0 if res == sys.maxsize else res


print(minSubArrayLen2(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen2(4, [1, 4, 4]))
print(minSubArrayLen2(11, [1, 2, 3, 4, 5]))
print(minSubArrayLen2(6, [10, 2, 3]))


def minSubArrayLen3(target, nums):
    n = len(nums)
    prefix_sum = nums[:]

    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]

    res = sys.maxsize
    for i in range(n - 1, -1, -1):
        if prefix_sum[i] < target: break
        tmp = prefix_sum[i] - target
        j = low_bound(i - 1, prefix_sum, tmp)
        res = min(res, i - j)

    return 0 if res == sys.maxsize else res


def low_bound(i, nums, target):
    l = 0
    r = i
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target or (nums[mid] < target and nums[mid + 1] > target): return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print("-" * 1000)
print(minSubArrayLen3(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen3(4, [1, 4, 4]))
print(minSubArrayLen3(11, [1, 2, 3, 4, 5]))
print(minSubArrayLen3(6, [10, 2, 3]))
