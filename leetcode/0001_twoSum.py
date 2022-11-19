# coding:utf-8

# 方案一
def twoSum0(nums, target):
    for i in range(len(nums)):
        sub = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == sub:
                return [i, j]

# 方案二
def twoSum1(nums, target):
    dict_nums = {}
    for i in range(len(nums)):
        dict_nums[target - nums[i]] = i

    for i in range(len(nums)):
        item = nums[i]
        if item in dict_nums and i != dict_nums[item]:
            return [i, dict_nums[item]]

# 方案三
def twoSum2(nums, target):
    dict_nums = {}
    for i in range(len(nums)):
        item = nums[i]
        dict_nums[target - item] = i
        if item in dict_nums and i != dict_nums[item]:
            return [dict_nums[item], i]


print(twoSum0([2, 7, 11, 15], 9))
print(twoSum1([2, 7, 11, 15], 9))
print(twoSum2([2, 7, 11, 15], 9))