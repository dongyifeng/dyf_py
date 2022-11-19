def max_profit(prices):
    result = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            result += prices[i] - prices[i - 1];
    return result


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

prices = [1, 2, 3, 4, 5]
print(max_profit(prices))
