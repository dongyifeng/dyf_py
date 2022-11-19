def longest_palindrome_subseq(s):
    n = len(s)
    if n == 1: return 1
    if n == 2 and s[0] == s[1]: return 2
    dp = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i + 1] = 1

    for k in range(2, n):
        i = 0
        while i + k < n:
            j = i + k
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            i += 1

    return dp[0][-1]


print(longest_palindrome_subseq("bbbab"))


def longest_palindrome_subseq2(s):
    n = len(s)
    if n == 1: return 1
    if n == 2 and s[0] == s[1]: return 2
    dp = [None for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i + 1] = 1

    for k in range(2, n):
        i = 0
        while i + k < n:
            j = i + k
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            i += 1

    return dp[0][-1]
