#!/usr/bin/python3
""" N queens """
import sys
from sys import exit


def queens(n, i=0, a=[], b=[], c=[]):
    """Find all possible positions for placing queens on the chessboard.

    Args:
        n (int): Size of the chessboard and the number of queens.
        i (int, optional): Current row being considered. Defaults to 0.
        a (list, optional): List of column positions for the queens.
                            Defaults to [].
        b (list, optional): List of diagonal positions (i + j) for the queens.
                            Defaults to [].
        c (list, optional): List of diagonal positions (i - j) for the queens.
                            Defaults to [].

    Yields:
        list: List of column positions for a valid arrangement of queens.
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
        list: List of solutions, each solution is a list of queen positions.

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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solve(n)
