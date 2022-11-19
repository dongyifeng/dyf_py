# 分组背包
# []
def knapsack(group, v):
    n = len(group)
    dp = [[0] * (v + 1) for _ in range(1 + n)]
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            dp[i][j] = dp[i][j - 1]
            for c, k in group[i - 1]:
                if j >= c:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - c] + k)
    for line in dp:
        print(line)

    return dp[-1][-1]


def knapsack2(group, v):
    n = len(group)
    dp = [0] * (v + 1)
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            dp[j] = dp[j - 1]
            for c, k in group[i - 1]:
                if j >= c:
                    dp[j] = max(dp[j], dp[j - c] + k)
    print(dp)
    return dp[-1]


group = [[(1, 2), (2, 3)], [(1, 1), (3, 5), (2, 4)]]
print(knapsack2(group, 8))
print(knapsack(group, 8))
