"""
Coin Change
-----------
Time:  O(amount * n) where n = number of coin types
Space: O(amount)

Given coins of different denominations and a total amount, find the
minimum number of coins needed. If it can't be made exactly, return -1.

This is the "fewest coins" variant — there's also the "count ways"
variant which is slightly different.
"""


def coin_change(coins, amount):
    """Returns minimum coins needed, or -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """Returns the number of distinct ways to make the amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
