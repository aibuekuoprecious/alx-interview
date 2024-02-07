#!/usr/bin/python3
import sys

N = 0

def is_safe(board, row, col):
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
