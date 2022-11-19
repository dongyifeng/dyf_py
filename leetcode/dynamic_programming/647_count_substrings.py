# 647. 回文子串
def count_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    res = 0
    for j in range(n):
        for i in range(j + 1):
            if j - i < 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
            if dp[i][j]:
                res += 1

    print(dp)
    return res


def count_substrings2(s):
    n = len(s)
    dp = [False] * n

    res = 0
    for j in range(n):
        for i in range(j + 1):
            if j - i < 2:
                dp[i] = s[i] == s[j]
            else:
                dp[i] = s[i] == s[j] and dp[i + 1]
            if dp[i]:
                res += 1

    return res


print(count_substrings("aaa"))

# for i in range(n):
#     dp[i][i] = 1
#     if i > 0:
#         if s[i] == s[i - 1]:
#             dp[i - 1][i] = 1
#         else:
#             dp[i - 1][i] = 0
#
# for i in range(2, n):
#     for j in range(j, n):
#         if s[i - 1] == s[j]:
#             dp[i][j] = 1
#         else:
#             dp[i][j] = 0
