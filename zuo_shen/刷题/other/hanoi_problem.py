'''
汉诺塔游戏的要求把所有的圆盘从左边都移到右边的柱子上，给定一个整型数组arr，其中只含有1、2、3，代表所有圆盘目前的状态，1 代表左柱，2代表中柱，3 代表右柱，arr[i] 的值代表第 i + 1 个圆盘的位置。
比如：arr = [3,3,2,1] ，代表第 1 个圆盘在右柱上，第 2 个圆盘在右柱上，第 3 个圆盘在中柱上，第 4 个圆盘在左柱上。
如果 arr 代表的状态是最优移动轨迹过程中出现的状态，返回 arr 这种状态是最优移动轨迹中第几状态；如果 arr 代表的状态不是最优移动轨迹过程中出现的状态，则返回 -1。
'''


def step(arr):
    if not arr: return 0
    return f(arr, len(arr) - 1, 1, 2, 3)


# 目标：把 arr[0~i] 的圆盘，从 from 全部挪到 to 上
# 返回：根据 arr 中状态 arr[0~i] ,它是最优解的第几步？
# 时间复杂度：O(N)
def f(arr, i, fro, other, to):
    if i == -1: return 0
    if arr[i] != fro and arr[i] != to:
        return -1
    if arr[i] == fro:
        # 第一大步没走完，arr[0~i-1] from --> other
        return f(arr, i - 1, fro, to, other)
    # 第三步完成的程度
    rest = f(arr, i - 1, other, fro, to)
    if rest == -1:
        return rest
    return (1 << i) + rest


def step1(arr):
    if not arr: return 0
    fro = 1
    other = 2
    to = 3
    i = len(arr) - 1
    res = 0
    while i >= 0:
        if arr[i] != fro and arr[i] != to: return -1
        if arr[i] == fro:
            res += 1 << i
            tmp = fro
            fro = other
        else:
            tmp = to
            to = other
        other = tmp
        i -= 1

    return res


import random


def check():
    for _ in range(1000):
        arr = [int(random.random() * 3) + 1 for _ in range(int(random.random() * 100))]
        res = step(arr)
        res1 = step(arr)
        if res != res1:
            print("ERROR","res=",res,"res1=",res1,arr)
    print("Nice")

check()