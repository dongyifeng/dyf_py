# coding:utf-8

# 全排列

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 输入: [1,2,3]
'''
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


def permute(nums):
    result = []
    backtrack(nums, result, 0)
    return result


def backtrack(nums, result, first):
    if first == len(nums):
        result.append(nums[:])

    for i in range(first, len(nums)):
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(nums, result, first + 1)
        nums[first], nums[i] = nums[i], nums[first]


print(permute([1, 2, 3]))


def permute2(nums):
    if len(nums)<2: return [nums]
    result = []

    for i, n in enumerate(nums):
        result.extend([n] + p for p in permute2(nums[:i] + nums[i + 1:]))
    return result


print(permute2([1, 2, 3]))
#
# for item in permute2([1, 2, 3]):
#     for i in item:
#         print(i)
