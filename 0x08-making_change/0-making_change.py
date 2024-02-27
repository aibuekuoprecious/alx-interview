#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    # Iterate through each coin denomination
    for coin in coins:
        # Update the minimum number of coins needed for each amount from the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If total cannot be met by any number of coins you have, return -1
    if dp[total] == float('inf'):
        return -1

    return dp[total]
