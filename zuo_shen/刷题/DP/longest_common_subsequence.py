'''
给定两个字符串 str1 和 str2 ，求两个字符串的最长公共子序列。
'''


def longest_common_subsequence(string1, string2):
    if not string1 or not string2: return 0
    return f(string1, string2, len(string1) - 1, len(string2) - 1)


def f(string1, string2, i, j):
    # base case
    if i < 0 or j < 0: return 0

    if i == 0 and j != 0:
        for k in range(j + 1):
            if string2[k] == string1[i]:
                return 1
        return 0

    if i != 0 and j == 0:
        for k in range(i + 1):
            if string1[k] == string2[j]:
                return 1
        return 0

    if string1[i] == string2[j]:
        return f(string1, string2, i - 1, j - 1) + 1

    return max(f(string1, string2, i, j - 1), f(string1, string2, i - 1, j))


def longest_common_subsequence1(string1, string2):
    if not string1 or not string2: return 0

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

    return dp[-1][-1]


def longest_common_subsequence2(string1, string2):
    if not string1 or not string2: return 0

    dp = [0] * len(string2)
    # base case
    dp[0] = 1 if string1[0] == string2[0] else 0

    for i in range(1, len(string2)):
        dp[i] = max(dp[i - 1], 1 if string1[0] == string2[i] else 0)

    for row in range(1, len(string1)):
        left_up = dp[0]
        dp[0] = max(dp[0], 1 if string2[0] == string1[row] else 0)
        for col in range(1, len(string2)):
            if string1[row] == string2[col]:
                new_value = left_up + 1
            else:
                new_value = max(dp[col - 1], dp[col])
            left_up = dp[col]
            dp[col] = new_value

    return dp[-1]


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
        res3 = longest_common_subsequence2(stirng1, stirng2)

        if res1 != res2 or res1 != res3:
            print("ERROR", stirng1, stirng2, "res1=", res1, "res2=", res2, "res3=", res3)
    print("OVER")


check()
# print(longest_common_subsequence("tt", "tg"))
# print(longest_common_subsequence2("tt", "tg"))
# print(longest_common_subsequence2("abefgh", "1a2b"))
