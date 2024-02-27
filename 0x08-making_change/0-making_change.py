#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make the given total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to be made.

    Returns:
        int: Minimum number of coins needed to make the total amount. 
        Returns -1 if it is not possible to make the total amount with the given coins.
    """
    
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
