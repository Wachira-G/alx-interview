#!/usr/bin/python3

"""Module for making change -coins."""

def makeChange(coins: list, total: int) -> int:
    """Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount (total)."""
    if total <= 0:
        return 0
    INF = float('inf')
    dp = [INF] * (total + 1)

    dp[0] = 0


    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i -coin])

    return dp[total] if dp[total] != INF else -1
