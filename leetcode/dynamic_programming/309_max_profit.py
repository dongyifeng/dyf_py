def max_profit(prices):
    n = len(prices)
    f = [0] * n
    k = [0] * n
    h = [0] * n

    f[0] = -prices[0]
    for i in range(1, n):
        f[i] = max(k[i - 1] - prices[i], f[i - 1])
        k[i] = max(h[i - 1], k[i - 1])
        h[i] = f[i - 1] + prices[i]

    return max(k[-1], h[-1])


def max_profit2(prices):
    n = len(prices)
    f = -prices[0]
    h = k = 0

    for i in range(1, n):
        tmp = max(k - prices[i], f)
        k = max(h, k)
        h = f + prices[i]
        f=tmp

    return max(k, h)


print(max_profit2([1, 2, 3, 0, 2]))
print(max_profit2([2, 1]))
