#!/usr/bin/python3
import sys


def solveNQueens(n):
    def can_place(pos, taken_pos):
        for i in range(len(taken_pos)):
            if (
                taken_pos[i] == pos
                or taken_pos[i] - i == pos - len(taken_pos)
                or taken_pos[i] + i == pos + len(taken_pos)
            ):
                return False
        return True

    def place_queens(n, index, taken_pos, all_taken_pos):
        if index == n:
            all_taken_pos.append(taken_pos[:])
            return

        for i in range(n):
            if can_place(i, taken_pos):
                taken_pos.append(i)
                place_queens(n, index + 1, taken_pos, all_taken_pos)
                taken_pos.pop()

    all_taken_pos = []
    place_queens(n, 0, [], all_taken_pos)
    return all_taken_pos


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

    solutions = solveNQueens(n)
    for solution in solutions:
        result = [[i, pos] for i, pos in enumerate(solution)]
        print(result)


if __name__ == "__main__":
    main()
