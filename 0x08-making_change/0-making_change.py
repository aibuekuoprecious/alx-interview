#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """Calculates the minimum number of coins needed 
    to make change for a given total value.
    """

    if total < 1:
        return 0

    coins.sort()
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
