# 322 零钱兑换
import sys


def coin_change(coins, amount):
    if amount <= 0: return 0
    dp = [sys.maxsize] * (amount + 1)

    for coin in coins:
        if coin <= amount:
            dp[coin] = 1

    for i in range(amount + 1):
        for coin in coins:
            if i - coin > 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[-1] if dp[-1] != sys.maxsize else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
print(coin_change([1], 1))
print(coin_change([1], 2))
