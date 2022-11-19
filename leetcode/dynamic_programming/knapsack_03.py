# 多重背包问题

def multiple_choice_knapsack3(c, w, n, v):
    l = len(c)
    dp = [] * (v + 1)
    for i in range(1, l + 1):
        for j in range(0, v + 1):
            dp[j] = dp[j]
            if j >= c[i - 1]:
                k = 1
                while j - k * c[i - 1] >= 0 and k <= n[i]:
                    dp[j] = max(dp[j], dp[j - k * c[i - 1]] + k * w[i - 1])
    return dp[-1]

def multiple_choice_knapsack2(c, w, n, v):
    l = len(c)
    dp = [[] * (v + 1) for _ in range(l + 1)]
    for i in range(1, l + 1):
        for j in range(0, v + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= c[i - 1]:
                k = 1
                while j - k * c[i - 1] >= 0 and k <= n[i]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * c[i - 1]] + k * w[i - 1])
    return dp[-1][-1]


def multiple_choice_knapsack(c, w, n, v):
    for i in n:
        c += [c[i]] * i
        w += [w[i]] * i

    return knapsack01(c, w, v)


def knapsack01(c, w, v):
    n = len(c)
    dp = [0] * (v + 1)

    for i in range(1, n + 1):
        for j in range(0, v + 1):
            if j >= c[i - 1]:
                dp[j] = max(dp[j], dp[j - c[i - 1]] + w[i - 1])

    return dp[-1]
