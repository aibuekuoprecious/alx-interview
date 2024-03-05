#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter of an island
represented in a 2D grid. The island is represented by 1s and the water is
represented by 0s. Cells outside the grid are also considered water.
"""

def calculate_island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    assert 1 <= num_rows and num_cols <= 100

    perimeter = 0
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if grid[row_index][col_index] == 1:  # Only consider land cells
                # Check upper neighbor
                if row_index == 0 or grid[row_index - 1][col_index] == 0:
                    perimeter += 1
                # Check left neighbor
                if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    perimeter += 1
                # Check lower neighbor
                if row_index == num_rows - 1 or grid[row_index + 1][col_index] == 0:
                    perimeter += 1
                # Check right neighbor
                if col_index == num_cols - 1 or grid[row_index][col_index + 1] == 0:
                    perimeter += 1

    return perimeter