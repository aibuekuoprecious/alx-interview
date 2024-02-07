import sys


def queens(n, i=0, a=[], b=[], c=[]):
    """
    Generates all valid solutions for placing 
    N queens on an N×N chessboard.

    Args:
        n (int): The size of the chessboard (N).
        i (int): The current row being considered.
        a (list): A list representing the current partial solution
                  (column indices of queens for each row).
        b (list): A list representing the diagonals 
                  from top-left to bottom-right.
        c (list): A list representing the diagonals
                  from top-right to bottom-left.

    Yields:
        list: A valid solution (list of column indices for each row).
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """
    Solves the N-queens problem and prints all solutions.

    Args:
        n (int): The size of the chessboard (N).
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
