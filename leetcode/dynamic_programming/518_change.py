# 518. 零钱兑换 II

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[-1]


print(change(5, [1, 2, 5]))
