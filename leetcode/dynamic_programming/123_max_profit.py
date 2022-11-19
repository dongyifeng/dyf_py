# 123. 买卖股票的最佳时机 III
# 错误
def max_profit(prices):
    n = len(prices)
    f = [0] * n
    k = [0] * n
    count = [0] * n
    f[0] = -prices[0]
    for i in range(1, n):
        f[i] = max(f[i - 1], k[i - 1] - prices[i])
        if k[i - 1] < f[i - 1] + prices[i]:
            k[i] = f[i - 1] + prices[i]
            count[i] = count[i - 1] + 1
        else:
            k[i] = k[i - 1]
            count[i] = count[i - 1]
    print(f)
    print(k)
    print(count)


max_profit([3, 3, 5, 0, 0, 3, 1, 4])
