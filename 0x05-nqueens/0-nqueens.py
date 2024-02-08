#!/usr/bin/env python3
""" Placing N non-attacking queens on an N×N chessboard"""

import sys


def solve_n_queens(n):
    def is_safe(queen, queens):
        for i in range(queen):
            if (
                queens[i] == queens[queen]
                or queens[i] - i == queens[queen] - queen
                or queens[i] + i == queens[queen] + queen
            ):
                return False
        return True

    def place_queen(queens, target_row):
        if target_row == n:
            result.append(queens[:])
            return
        for column in range(n):
            queens[target_row] = column
            if is_safe(target_row, queens):
                place_queen(queens, target_row + 1)

    result = []
    place_queen([0] * n, 0)
    return result


def print_result(result):
    for solution in result:
        print([[row, col] for row, col in enumerate(solution)])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    result = solve_n_queens(n)
    print_result(result)


if __name__ == "__main__":
    main()
