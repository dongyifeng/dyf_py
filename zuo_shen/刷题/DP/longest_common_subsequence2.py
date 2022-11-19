'''
给定两个字符串 str1 和 str2 ，求两个字符串的最长公共子序列。
'''


class Info:
    def __init__(self, length, res):
        self.length = length
        self.res = res


def longest_common_subsequence(string1, string2):
    if not string1 or not string2: return ""
    info = f(string1, string2, len(string1) - 1, len(string2) - 1)
    return ''.join(info.res)


def f(string1, string2, i, j):
    # base case
    if i < 0 or j < 0: return Info(0, [])

    if i == 0 and j != 0:
        for k in range(j + 1):
            if string2[k] == string1[i]:
                return Info(1, [string2[k]])
        return Info(0, [])

    if i != 0 and j == 0:
        for k in range(i + 1):
            if string1[k] == string2[j]:
                return Info(1, [string1[k]])
        return Info(0, [])

    if string1[i] == string2[j]:
        info = f(string1, string2, i - 1, j - 1)
        res = info.res[:]
        res.append(string1[i])

        return Info(info.length + 1, res)

    info1 = f(string1, string2, i, j - 1)
    info2 = f(string1, string2, i - 1, j)

    length = info1.length
    res = info1.res[:]
    if info2.length > length:
        length = info2.length
        res = info2.res[:]

    return Info(length, res)


def longest_common_subsequence1(string1, string2):
    if not string1 or not string2: return ""

    dp = [[0] * len(string2) for _ in range(len(string1))]

    # base case
    dp[0][0] = 1 if string1[0] == string2[0] else 0
    for i in range(1, len(string1)):
        dp[i][0] = max(dp[i - 1][0], 1 if string1[i] == string2[0] else 0)

    for i in range(1, len(string2)):
        dp[0][i] = max(dp[0][i - 1], 1 if string1[0] == string2[i] else 0)

    for row in range(1, len(string1)):
        for col in range(1, len(string2)):
            if string1[row] == string2[col]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

    row = len(string1) - 1
    col = len(string2) - 1

    index = dp[-1][-1]
    res = [None] * index
    while index > 0:
        if row > 0 and dp[row][col] == dp[row - 1][col]:
            row -= 1
        elif col > 0 and dp[row][col] == dp[row][col - 1]:
            col -= 1
        else:
            index -= 1
            res[index] = string1[row]
            row -= 1
            col -= 1

    return ''.join(res)


import random


def generator_random_str(max_size):
    alphabet = [chr(i) for i in range(97, 123)]
    size = int(random.random() * max_size)
    return ''.join([random.sample(alphabet, 1)[0] for _ in range(size)])


def check():
    max_size = 10
    for i in range(500):
        stirng1 = generator_random_str(max_size)
        stirng2 = generator_random_str(max_size)

        res1 = longest_common_subsequence(stirng1, stirng2)
        res2 = longest_common_subsequence1(stirng1, stirng2)

        if len(res1) != len(res2):
            print("ERROR", stirng1, stirng2, "res1=", res1, "res2=", res2)
    print("OVER")


check()
# print(longest_common_subsequence("tt", "tg"))
# print(longest_common_subsequence2("tt", "tg"))
# print(longest_common_subsequence("abefgh", "1a2b"))
# print(longest_common_subsequence1("abefgh", "1a2b"))
