# 二维费用的背包问题
def knapsack(c1, c2, w, v1, v2):
    n = len(w)
    dp = [[[0] * (v1 + 1) for _ in range(v2 + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(v2 + 1):
            for k in range(v1 + 1):
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - c2[i]][k - c1[i]] + w[i])

    return dp[-1][-1][-1]
