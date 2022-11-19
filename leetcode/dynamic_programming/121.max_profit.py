def max_profit(prices):
    result = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            result = max(result, prices[j] - prices[i])
    return result


import sys


def max_profit2(prices):
    min_value = sys.maxsize
    result = 0
    for i in range(len(prices)):
        min_value = min(min_value, prices[i])
        result = max(prices[i] - min_value, result)
    return result


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit2([7, 1, 5, 3, 6, 4]))
