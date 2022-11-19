# 有依赖的背包问题

def knapsack(W, V):
    # 去掉依赖
    for i in range(len(W)):
        v, w, p = W[i]
        if p == -1: continue
        p_p = p
        new_v = v
        new_w = w
        while p_p != -1:
            p_v, p_w, p_p = W[p_p]
            new_v += p_v
            new_w += p_w
        W[i] = [new_v, new_w, -1]

    return knapsack01(W, V)


def knapsack01(W, v):
    n = len(W)
    dp = [0] * (v + 1)

    for i in range(1, n + 1):
        for j in range(0, v + 1):
            if j >= W[i - 1][0]:
                dp[j] = max(dp[j], dp[j - W[i - 1][0]] + W[i - 1][1])

    return dp[-1]


W = [[2, 3, -1],
     [2, 2, 0],
     [3, 5, 0],
     [4, 7, 1],
     [3, 6, 1]]
V = 7
print(knapsack(W, V))
