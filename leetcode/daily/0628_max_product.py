# 三个数的最大乘积

# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

'''
示例 1:
输入: [1,2,3]
输出: 6


示例 2:
输入: [1,2,3,4]
输出: 24
'''



def maximumProduct(nums):
    sorted_nums = sorted(nums)
    return max(sorted_nums[-1] * sorted_nums[0] * sorted_nums[1], sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3])


print(maximumProduct([-100, -98, -1, 2, 3, 4]))
