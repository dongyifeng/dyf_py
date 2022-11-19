# 剑指 Offer 63. 股票的最大利润

def max_profit(prices):
    n = len(prices)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    return res


def max_profit2(prices):
    if not prices: return 0
    res = 0
    min_value = prices[0]
    for p in prices:
        min_value = min(min_value, p)
        res = max(res, p - min_value)
    return res


print(max_profit2([7, 1, 5, 3, 6, 4]))
print(max_profit2([7, 6, 4, 3, 1]))
