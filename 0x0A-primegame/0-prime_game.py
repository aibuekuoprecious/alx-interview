#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Determines the winner of a prime game.
    """

    if x <= 0 or x != len(nums) or nums is None:
        return None

    ben = 0
    maria = 0

    for num in nums:
        if isPrime(num):
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
