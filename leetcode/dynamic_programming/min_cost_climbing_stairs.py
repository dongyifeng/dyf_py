
'''
爬楼梯的最少成本

数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
'''


def min_cost_climbing_stairs(nums):
    if len(nums) == 0: return 0
    s1 = 0
    s2 = min(nums[:2])
    res = min(s1 + nums[0], s2 )
    for i in range(2, len(nums)):
        res = min(s1 + nums[i - 1], s2 + nums[i])
        s1 = s2
        s2 = res

    return res


print(min_cost_climbing_stairs([10, 15, 20]))
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(min_cost_climbing_stairs([1, 100]))
print(min_cost_climbing_stairs([4, 1]))
