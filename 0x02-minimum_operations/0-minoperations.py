#!/usr/bin/python3
""" Module for 0-minoperations """

def minOperations(n):
    """ Calculates the fewest number of operations needed """
    if (n < 2):
        return 0
    
    operations = 0
    clipboard = 0
    currentChar = 1

    while currentChar< n:
        if n % currentChar == 0:
            # Copy All
            operations += 1
        # Paste
        operations += 1
    
    # Check if n is a prime number
    if currentChar < n:
        operations += 1

    return operations
