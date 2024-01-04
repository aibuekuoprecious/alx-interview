#!/usr/bin/python3
"""
Pascal's Triangle

This script defines a function `pascal_triangle(n)` that generates Pascal's triangle
up to the specified number of rows, `n`. The function returns a list of lists
representing the triangle.

Usage:
    result = pascal_triangle(n)
    print(result)
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows, n.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists.
    """
    result = []

    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            result.append(level)

    return result