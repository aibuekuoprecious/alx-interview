#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """Find all possible positions for placing n queens on an n x n chessboard.

    Args:
        n (int): The size of the chessboard and the number of queens to be placed.
        i (int, optional): The current row being considered. Defaults to 0.
        a (list, optional): The list of column positions for the queens in each row.
                            Defaults to [].
        b (list, optional): The list of diagonal positions 
                            (sum of row and column) for the queens.
                            Defaults to [].
        c (list, optional): The list of diagonal positions 
                            (difference of row and column) for the queens.
                            Defaults to [].

    Yields:
        list: A list of column positions for the queens in each row,
              representing a valid solution.

    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """
    Solve the N-Queens problem and return a list of solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of queen positions.

    """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
