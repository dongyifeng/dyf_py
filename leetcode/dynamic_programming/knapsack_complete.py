# 完全背包问题：
# 有 N 种物品和一个容量为 V 的背包，每种物品都有无限件可用。第 i 种物品的体积是 c[i]，价值是 w[i]。求解将哪些物品装入背包可使这些物品的总体积和不超过背包容量，且价值总和最大。

def knapsack_complete(c, w, v):
    n = len(c)
    dp = [[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, v + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= c[i - 1]:
                k = 1
                while j - k * c[i - 1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * c[i - 1]] + k * w[i - 1])
                    k += 1

    return dp[-1][-1]


def knapsack_complete2(c, w, v):
    n = len(c)
    dp = [0] * (v + 1)

    for i in range(1, n + 1):
        for j in range(0, v + 1):
            if j >= c[i - 1]:
                k = 1
                while j - k * c[i - 1] >= 0:
                    dp[j] = max(dp[j], dp[j - k * c[i - 1]] + k * w[i - 1])
                    k += 1

    return dp[-1]


def knapsack_complete3(c, w, v):
    n = len(c)
    print(c)
    print(w)
    print(v)
    for i in range(n):
        num = int(v / c[i]) - 1
        c += [c[i]] * num
        w += [w[i]] * num

    return knapsack01(c, w, v)


def knapsack01(c, w, v):
    n = len(c)
    dp = [0] * (v + 1)

    for i in range(1, n + 1):
        for j in range(0, v + 1):
            if j >= c[i - 1]:
                dp[j] = max(dp[j], dp[j - c[i - 1]] + w[i - 1])

    return dp[-1]


c = [5, 7]
w = [5, 8]
v = 10
print(knapsack_complete3(c, w, v))
