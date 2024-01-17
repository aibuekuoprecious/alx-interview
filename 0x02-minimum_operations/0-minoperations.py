#!/usr/bin/python3
"""
Module for 0-minoperations

This module contains a function that calculates the minimum number of operations
needed to result in exactly n H characters in a text file using a text editor
that can only execute two operations: Copy All and Paste.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    operations (int): The minimum number of operations. If n is less than 2, it returns 0.
    """
    if (n < 2):
        return 0
    
    operations = 0
    clipboard = 0
    currentChar = 1

    while currentChar< n:
        if n % currentChar == 0:
            # Copy All
            clipboard = currentChar
            operations += 1
        # Paste
        currentChar += clipboard
        operations += 1
    
    # Check if n is a prime number
    if currentChar < n:
        operations += 1

    return operations
