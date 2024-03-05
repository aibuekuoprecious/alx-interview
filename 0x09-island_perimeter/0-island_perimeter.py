#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""

def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    num_rows = len(grid)
    num_cols = len(grid[0])
    assert 1 <= num_rows and num_cols <= 100

    perimeter = 0
    for i in range(num_rows):
        for j in range(num_cols):
            assert grid[i][j] == 0 or grid[i][j] == 1
            if i - 1 < 0:
                perimeter += 1
            else:
                perimeter += grid[i - 1][j]
            if j - 1 < 0:
                perimeter += 1
            else:
                perimeter += grid[i][j - 1]

            try:
                perimeter += grid[i + 1][j]
            except IndexError:
                perimeter += 1
            try:
                perimeter += grid[i][j + 1]
            except IndexError:
                perimeter += 1

    return perimeter