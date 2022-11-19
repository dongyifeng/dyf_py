'''
给定一个数组 arr，代表一排有分数的气球。每打爆一个气球都能获得分数，假设打爆气球的分数为 X，获得分数的规则如下：

1. 如果被打爆气球的左边有没打爆的气球，找到离被打爆气球最近的气球，假设分数为 L；如果被打爆气球的右边有没有打爆的气球，找到离被打爆气球最近的气球，假设分数为 R。获得分数为 L * X * R
2. 如果被打爆气球的左边有没打爆的气球，找到离被打爆气球最近的气球，假设分数为 L；如果被打爆气球的右边所有气球都已经被打爆。获得分数为：L*X
3. 如果被打爆气球的左边所有气球都已经被打爆；如果被打爆气球的右边有没有打爆的气球，找到离被打爆气球最近的气球，假设分数为 R。获得分数为：R*X
4. 如果被打爆气球的左边和右边所有气球都已经被打爆。获得分数为：X

目标是打爆所有气球，返回能获得的最大分数。

【举例】

arr =【3,2,5】

- 如果先打爆 3，获得 3\*2；再打爆 2，获得 2\* 5 ;最后打爆 5 ，获得 5；总分为：6+10+5=21.
- 如果先打爆 3，获得 3\*2；再打爆 5，获得 2\* 5 ;最后打爆 2 ，获得 2；总分为：6+10+2=18.
- 如果先打爆 2，获得 3\*2*5；再打爆 3，获得 3\* 5 ;最后打爆 5 ，获得 5；总分为：30+15+5=50.
- 如果先打爆 2，获得 3\*2*5；再打爆 5，获得 3\* 5 ;最后打爆 3 ，获得 3；总分为：30+15+3=48.
- 如果先打爆 5，获得 2\*5；再打爆 3，获得 3\* 2 ;最后打爆 2 ，获得 2；总分为：10+6+2=18.
- 如果先打爆 5，获得 2\*5；再打爆 2，获得 3\* 2 ;最后打爆 3 ，获得 3；总分为：10+6+3=19.

返回最大分数为 50
'''


def max_score(arr):
    if not arr: return 0
    # 哨兵，因为 f 要求 arr[l-1] 和 arr[r+1] 一定没有被打破
    arr.insert(0, 1)
    arr.append(1)
    return f(arr, 1, len(arr) - 2)


# 打爆 arr[l...r] 范围上的所有气球，返回最大的分数
# 假设arr[l-1] 和 arr[r+1] 一定没有被打破
def f(arr, l, r):
    # 如果 arr[l...r] 范围上只有一个气球，直接打爆即可
    if l == r:
        return arr[l - 1] * arr[l] * arr[r + 1]

    # 最后打爆 arr[l] 的方案 和 最后打爆 arr[r] 的方案，先比较一下
    res = max(arr[l - 1] * arr[l] * arr[r + 1] + f(arr, l + 1, r),
              arr[l - 1] * arr[r] * arr[r + 1] + f(arr, l, r - 1))

    # 尝试中间位置的气球最后打爆的每一种方案
    for k in range(l + 1, r):
        res = max(res, arr[l - 1] * arr[k] * arr[r + 1] + f(arr, l, k - 1) + f(arr, k + 1, r))

    return res


def max_score2(arr):
    if not arr: return 0
    arr.insert(0, 1)
    arr.append(1)
    dp = [[None] * (len(arr)) for _ in range(len(arr))]
    for i in range(1, len(arr) - 1):
        dp[i][i] = arr[i - 1] * arr[i] * arr[i + 1]

    for row in dp:
        print(row)

    for l in range(len(arr) - 3, 0, -1):
        for r in range(l + 1, len(arr) - 1):
            res = max(arr[l - 1] * arr[l] * arr[r + 1] + f(arr, l + 1, r),
                      arr[l - 1] * arr[r] * arr[r + 1] + f(arr, l, r - 1))
            for k in range(l + 1, r):
                res = max(res, arr[l - 1] * arr[k] * arr[r + 1] + f(arr, l, k - 1) + f(arr, k + 1, r))
        dp[l][r] = res


    print('-'*1000)
    for row in dp:
        print(row)

    return dp[1][len(arr) - 2]


import random


def generator_random_arr(max_size, max_value):
    return [item for item in
            set([int(random.random() * max_value) + 1 for _ in range(int(random.random() * max_size) + 1)])]


def check():
    global map
    max_size = 5
    max_value = 10
    for _ in range(10000):
        arr = generator_random_arr(max_size, max_value)
        # print("info2", aim, arr)
        res = max_score(arr[:])
        res2 = max_score2(arr[:])
        # print("Info", "res=", res, "res2=", res2, aim, arr)
        if res != res2 or res != res2:
            print("ERROR", "res=", res, "res2=", res2, arr)
    print("OVER")


# check()

print(max_score([1, 1, 2, 1, 1]))
print(max_score2([1, 1, 2, 1, 1]))
