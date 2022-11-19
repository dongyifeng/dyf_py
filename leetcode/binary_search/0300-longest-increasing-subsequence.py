# coding=utf-8
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


# 动态规划
def length_of_lis(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
# 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))
#

print(length_of_lis([4, 10, 4, 3, 8, 9]))


# 贪心算法 + 二分查找
def length_of_lis2(nums):
    n = len(nums)
    if n == 0: return 0
    res = 1
    dp = [0] * n
    dp[res] = nums[0]

    for i in range(1, n):
        if nums[i] > dp[res]:
            res += 1
            dp[res] = nums[i]
            continue

        l = 1
        r = res
        pos = 0
        while l <= r:
            mid = (l + r) >> 1
            if dp[mid] < nums[i]:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        dp[pos + 1] = nums[i]

    return res


print(length_of_lis2([10, 9, 2, 5, 3, 7, 101, 18]))
