'''
给定两个字符串 str1 和 str2 ，再给定三个整数 ic 、dc、rc，分别代表插入、删除、替换一个字符的代价，返回将 str1 编辑成 str2 的最小代价。

【举例】

str1= “abc”，str2= “adc”，ic=5，dc=3，rc=2

从 “abc” 编辑成 “adc” ,把 “b” 替换成 “d” 是代价最小的，所以返回 2

str1= “abc”，str2= “adc”，ic=5，dc=3，rc=100

从 “abc” 编辑成 “adc” ,先删除 “b”，再插入 “d” 是代价最小的，所以返回 8

str1= “abc”，str2= “abc”，ic=5，dc=3，rc=2

不需要编辑了，本来就是一样的字符串，所以返回 0
'''


def min_cost(str0, str1, insert_cost, delete_cost, replace_cost):
    if not str0 or not str1: return 0

    row = len(str0) + 1
    col = len(str1) + 1

    dp = [[0] * col for _ in range(row)]

    for i in range(1, col):
        dp[0][i] = i * insert_cost

    for i in range(1, row):
        dp[i][0] = i * delete_cost

    for i in range(1, row):
        for j in range(1, col):
            if str0[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + replace_cost

            dp[i][j] = min(dp[i][j], dp[i][j - 1] + insert_cost)
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + delete_cost)

    return dp[-1][-1]


str1 = "abc"
str2 = "adc"
ic = 5
dc = 3
rc = 2
print(min_cost(str1, str2, ic, dc, rc))

str1 = "abc"
str2 = "adc"
ic = 5
dc = 3
rc = 100
print(min_cost(str1, str2, ic, dc, rc))

str1 = "abc"
str2 = "abc"
ic = 5
dc = 3
rc = 2
print(min_cost(str1, str2, ic, dc, rc))
