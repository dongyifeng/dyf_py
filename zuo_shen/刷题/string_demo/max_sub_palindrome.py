'''
给定一个字符串 str，求最长的<font color=green>回文子序列</font>。
'''


def max_sub_palindrome(string):
    if not string: return 0
    t = f(string, 0, len(string) - 1)
    return t


def f(string, i, j):
    if i == j:
        return 1
    if i == j + 1 or i + 1 == j:
        return 2 if string[i] == string[j] else 1

    if string[i] == string[j]:
        return f(string, i + 1, j - 1) + 2
    return max(f(string, i + 1, j), f(string, i, j - 1))


def max_sub_palindrome2(string):
    if not string: return 0
    n = len(string)
    dp = [[0] * n for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # for row in dp:
    #     print(row)
    return dp[0][-1]


def max_sub_palindrome3(string):
    if not string: return 0
    n = len(string)
    dp = [1] * n

    for i in range(n - 2, -1, -1):
        tmp = 0
        for j in range(i + 1, n):
            if string[i] == string[j]:
                new_value = tmp + 2
                tmp = dp[j]
                dp[j] = new_value
            else:
                new_value = max(dp[j], dp[j - 1])
                tmp = dp[j]
                dp[j] = new_value

    return dp[-1]


def max_sub_palindrome4(string):
    if not string: return ""
    n = len(string)
    dp = [[0] * n for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    count = row = 0
    col = n - 1
    res_len = index = dp[row][col]
    res = [None] * index
    while count < res_len:
        if row < n - 1 and dp[row][col] == dp[row + 1][col]:
            row += 1
        elif col > 0 and dp[row][col] == dp[row][col - 1]:
            col -= 1
        else:
            index -= 1
            res[res_len - index - 1] = res[index] = string[row]
            count += 2
            row += 1
            col -= 1
    return res


import random


def generator_random_str(max_size):
    alphabet = [chr(i) for i in range(97, 123)]
    size = int(random.random() * max_size)
    return ''.join([random.sample(alphabet, 1)[0] for _ in range(size)])


def check():
    max_size = 10
    for i in range(500):
        stirng1 = generator_random_str(max_size)

        res1 = max_sub_palindrome(stirng1)
        res2 = max_sub_palindrome2(stirng1)
        res3 = max_sub_palindrome3(stirng1)
        res4 = max_sub_palindrome4(stirng1)

        if res1 != res2 or  res1 != res3 or res1 != len(res4):
            print("ERROR", stirng1, "res1=", res1, "res2=", res2, "res3=", res3,"res4=", res4)
    print("OVER")


check()

# print(max_sub_palindrome("ttxt"))
# print(max_sub_palindrome2("ttxt"))
# print(max_sub_palindrome3("ttxt"))
