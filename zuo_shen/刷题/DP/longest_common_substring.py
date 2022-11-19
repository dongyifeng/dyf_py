'''
给定两个字符串 str1 和 str2 ，求两个字符串的最长公共子串。
'''


class Info:
    def __init__(self, length, res, end):
        self.length = length
        self.res = res
        self.end = end


def longest_common_substring(string1, string2):
    if not string1 or not string2: return ""
    col = len(string2) - 1
    row = 0
    res = end = 0
    while col >= 0:
        i = row
        j = col

        info = f(string1, string2, i, j)
        if info.res > res:
            res = info.res
            end = info.end

        if row < len(string1) - 1:
            row += 1
        else:
            col -= 1

    return string1[end - res + 1:end + 1]


def f(string1, string2, i, j):
    if i == 0 or j == 0:
        num = 1 if string1[i] == string2[j] else 0
        return Info(num, num, i)
    info = f(string1, string2, i - 1, j - 1)
    length = info.length + 1 if string1[i] == string2[j] else 0
    if length > info.res:
        return Info(length, length, i)
    return Info(length, info.res, info.end)


def longest_common_substring2(string1, string2):
    if not string1 or not string2: return ""
    dp = [[0] * len(string2) for _ in range(len(string1))]

    res = end = 0
    # base case
    for i in range(len(string1)):
        if string1[i] == string2[0]:
            res = dp[i][0] = 1
            end = i
    for i in range(len(string2)):
        if string1[0] == string2[i]:
            res = dp[0][i] = 1
            end = 0

    for row in range(1, len(string1)):
        for col in range(1, len(string2)):
            dp[row][col] = dp[row - 1][col - 1] + 1 if string1[row] == string2[col] else 0
            if dp[row][col] > res:
                res = dp[row][col]
                end = row

    return string1[end - res + 1:end + 1]


def longest_common_substring3(string1, string2):
    if not string1 or not string2: return ""
    dp = [0] * len(string2)

    res = end = 0
    # base case
    for i in range(len(string2)):
        dp[i] = 1 if string1[0] == string2[i] else 0
        if string1[0] == string2[i]:
            res = dp[i] = 1
            end = 0

    for row in range(1, len(string1)):
        for col in range(len(string2) - 1, 0, -1):
            dp[col] = dp[col - 1] + 1 if string1[row] == string2[col] else 0
            if dp[col] > res:
                res = dp[col]
                end = row

        dp[0] = 1 if string1[row] == string2[0] else 0
        if dp[0] > res:
            res = dp[0]
            end = row

    return string1[end - res + 1:end + 1]


def longest_common_substring4(string1, string2):
    if not string1 or not string2: return ""
    row = 0
    col = len(string2) - 1

    res = end = 0
    while row < len(string1):
        i = row
        j = col
        length = 0
        while i < len(string1) and j < len(string2):
            length = length + 1 if string1[i] == string2[j] else 0
            if length > res:
                res = length
                end = i

            i += 1
            j += 1

        if col > 0:
            col -= 1
        else:
            row += 1

    return string1[end - res + 1:end + 1]


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

        res1 = longest_common_substring(stirng1, stirng2)
        res2 = longest_common_substring2(stirng1, stirng2)
        res3 = longest_common_substring3(stirng1, stirng2)
        res4 = longest_common_substring4(stirng1, stirng2)

        if len(res1) != len(res2) or len(res1) != len(res3) or len(res1) != len(res4):
            print("ERROR", stirng1, stirng2, "res1=", res1, "res2=", res2, "res3=", res3, "res4=", res4)
    print("OVER")


check()
