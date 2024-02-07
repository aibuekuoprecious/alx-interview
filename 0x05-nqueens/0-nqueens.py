#!/usr/bin/python3
"""
Placing N non-attacking queens on an N×N chessboard
"""
import sys

N = 0


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position on the board.

    Args:
        board (list): The chess board represented as a 2D list.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.

    Returns:
        bool: True if it is safe to place a queen at the given position,
        False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nq(board, col):
    """
    Solve the N-Queens problem recursively.

    Args:
        board (list): The N x N chessboard represented as a 2D list.
        col (int): The current column being considered.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == N:
        print(board)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nq(board, col + 1) or res
            board[i][col] = 0
    return res


def solve_nq_util():
    """
    Utility function for solving the N-queens problem.
    """
    global N
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(N)] for j in range(N)]
    if not solve_nq(board, 0):
        print("Solution does not exist")
        sys.exit(0)


solve_nq_util()
