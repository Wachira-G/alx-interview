#!/usr/bin/python3

"""Module for making change -coins."""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Calculate the fewest number of coins needed to meet the given total amount.

    Args:
        coins (list[int]): List of coin values.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
            If total is 0 or less, returns 0.
            If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Dynamic programming approach
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if the total amount can be achieved
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
