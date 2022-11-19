def max_profit(prices, fee):
    n = len(prices)
    f = [0] * n
    k = [0] * n
    f[0] = -prices[0]
    for i in range(1, n):
        f[i] = max(f[i - 1], k[i - 1] - prices[i])
        k[i] = max(f[i - 1] + prices[i] - fee, k[i - 1])

    return k[-1]


def max_profit2(prices, fee):
    n = len(prices)
    f = -prices[0]
    k = 0
    for i in range(1, n):
        tmp = max(f, k - prices[i])
        k = max(k, f + prices[i] - fee)
        f = tmp

    return k


print(max_profit([1, 3, 2, 8, 4, 9], 2))
print(max_profit([1, 3, 7, 5, 10, 3], 3))

print(max_profit2([1, 3, 2, 8, 4, 9], 2))
print(max_profit2([1, 3, 7, 5, 10, 3], 3))
