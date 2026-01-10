coins = [1,2,5]
amount = 11

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for coin in coins:
    for current_amount in range(coin, amount + 1):
        dp[current_amount] = min(
            dp[current_amount],
            dp[current_amount - coin] + 1
        )

print(dp[amount])  # → 3
