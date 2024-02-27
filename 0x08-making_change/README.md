# Coin Change Problem

## Description

This Python function, `makeChange(coins, total)`, solves the coin change problem. Given a pile of coins of different values, it determines the fewest number of coins needed to meet a given amount total.

- If the total is 0 or less, it returns 0.
- If the total cannot be met by any combination of coins, it returns -1.
- The function assumes an infinite number of each denomination of coin in the list.

## Usage

```python
from make_change import makeChange

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print("Fewest number of coins needed:", result)  # Output: 3 (11 = 5 + 5 + 1)