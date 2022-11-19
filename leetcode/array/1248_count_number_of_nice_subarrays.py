# coding:utf-8

'''
统计「优美子数组」

https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def numberOfSubarrays(nums, k2):
    p = 0
    result = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            p += 1
            continue
        c = 0
        for k in range(i, len(nums)):
            if nums[k] % 2 == 0:
                continue
            c += 1
            if c == k2:
                c2 = 0
                for s in range(k + 1, len(nums)):
                    if nums[s] % 2 == 1: break
                    c2 += 1
                result += (p + 1) * (c2 + 1)
                p = 0
                break

    return result


def findSub(nums, start, k):
    p = 0
    c = 0
    m = start - 1
    for i in range(start, len(nums)):
        if nums[i] % 2 == 0:
            p += 1
            continue
        if m <= start: m = start
        c += 1
        if c == k: break
    return (p, m, c)


# print(numberOfSubarrays([1, 1, 1, 1, 1], 1))
#
# print(numberOfSubarrays([1, 1, 2, 1, 1], 3))
# print(numberOfSubarrays([2, 4, 6], 1))
# print(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))


print(findSub([1, 1, 1, 1, 1], 0,1))
