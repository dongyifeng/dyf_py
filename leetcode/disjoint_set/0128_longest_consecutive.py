# 128. 最长连续序列

'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。


示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
'''


def longest_consecutive(nums):
    parents = {}
    nums_set = set(nums)

    for item in nums_set:
        if item - 1 in nums_set:
            parents[item] = item - 1

    res = 0
    for item in nums_set:
        res = max(res, find_count(item, parents, 1))
    return res


def find_count(item, parents, c):
    if item not in parents.keys():
        return c
    return find_count(parents[item], parents, c + 1)


def longest_consecutive2(nums):
    parents = {}
    nums_set = set(nums)

    for item in nums_set:
        if item - 1 in nums_set:
            parents[item] = item - 1

    res = 0
    memo = {}
    for item in nums_set:
        tmp = item
        count = 1
        while tmp in parents:
            if tmp in memo:
                count += memo[tmp] - 1
                break
            count += 1
            tmp = parents[tmp]
        res = max(res, count)
        memo[item] = count

    return res


# print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
