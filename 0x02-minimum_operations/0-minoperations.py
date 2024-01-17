#!/usr/bin/python3
""" Module for 0-minoperations """

def minOperations(n):
    """ Calculates the fewest number of operations needed """
    if (n < 2):
        return 0
    
    operations = 0
    currentChar = 1

    while currentChar < n:
        if n % currentChar == 0:
            # Copy All
            operations += 1
            currentChar += currentChar  # Paste after Copy All
        else:
            # Paste
            currentChar += currentChar
        operations += 1

    return operations
