#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise
    Args:
        matrix (list[list]): A 2D matrix
    Returns:
        list[list]: The rotated matrix
    """
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - i - 1] = matrix[i][j]
    return rotated_matrix
