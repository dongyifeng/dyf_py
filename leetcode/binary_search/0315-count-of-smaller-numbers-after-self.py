# coding=utf-8

'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
'''

'''
暴力解法：O(n^2)
'''


def countSmaller(nums):
    n = len(nums)
    counts = [0 for i in range(n)]
    for i in range(n):
        c = 0
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                c += 1
        counts[i] = c
    return counts



def countSmaller2(nums):
    n = len(nums)
    counts = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            counts[i] = counts[i + 1] + 1
        else:
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    counts[i] = counts[j] + 1
    return counts


# print countSmaller([5, 2, 6, 1])

print(countSmaller([5, 2, 6, 1]))

print(countSmaller([0, 2, 1]))

print(countSmaller([2, 0, 1]))

print("-" * 100)

print(countSmaller2([5, 2, 6, 1]))

print(countSmaller2([0, 2, 1]))

print(countSmaller2([2, 0, 1]))
