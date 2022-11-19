'''
给定一个整型数组 arr，代表数值不同的纸牌排成一条线。玩家 A 和 玩家 B 依次拿走每张纸牌，规定玩家 A 先拿，玩家 B 后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家 A 和 玩家 B 都绝顶聪明。请返回最后获胜者的分数。

【举例】arr = 【1    	2	100     4】开始时，玩家 A  只能拿走 1 或 4 。如果开始时玩家 A 只能拿走 1，则排列变为【2	100	4】，接下来玩家 B 可以拿走 2 或 4，然后继续轮到玩家 A...

如果开始时玩家 A 拿走 4，则排列变为【1	2	100】，接下来玩家 B 可以拿走 1 或 100，然后继续轮到玩家 A...

玩家 A 作为绝顶聪明的人不会先拿走 4，因为拿走 4 之后，玩家 B 将拿走 100。所以玩家 A 会先拿 1，让排列变为【2	100	4】，接下来玩家 B 不管怎么选，100 都会被玩家 A 拿走。玩家 A 会获胜，分数为 101。所以返回 101

arr =【1	100	2】 开始时，玩家 A 不管拿 1 还是 2，玩家 B 作为绝顶聪明的人，都会把 100 拿走。玩家 B 会获胜，分数100。所以返回 100。
'''


def win(nums):
    if not nums: return 0

    return max(f(nums, 0, len(nums) - 1), s(nums, 0, len(nums) - 1))


# 玩家 A 拿牌
def f(nums, left, right):
    if left == right:
        return nums[left]
    return max(nums[left] + s(nums, left + 1, right), nums[right] + s(nums, left, right - 1))


# 玩家 B 拿牌
def s(nums, left, right):
    if left == right:
        return 0
    return min(f(nums, left + 1, right), f(nums, left, right - 1))


def win2(nums):
    if not nums: return 0
    n = len(nums)
    f = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for i in range(n):
        f[i][i] = nums[i]
    for i in range(1, n):
        for j in range(n):
            if i + j >= n: break
            left = j
            right = i + j
            f[left][right] = max(nums[left] + s[left + 1][right], nums[right] + s[left][right - 1])
            s[left][right] = min(f[left + 1][right], f[j][right - 1])

    return max(f[0][-1], s[0][-1])


import random


def random_array_generator(max_size, max_value):
    return [int(random.random() * max_value + 1) for _ in range(int(random.random() * max_size + 1))]


def check():
    n = 200
    max_size = 20
    max_value = 20

    for i in range(n):
        nums = random_array_generator(max_size, max_value)
        if win(nums) != win2(nums):
            print("ERROR", win2(nums), win(nums), nums)
    print("Game Over!")


check()
# nums = [1, 6, 1]
# print(win(nums))
# print(win2(nums))
