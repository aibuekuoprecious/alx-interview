#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys


def generate_solutions(n):
    """Generate all possible solutions for placing n queens on an n x n chessboard"""
    solutions = [[]]  # Initialize solutions as a list of empty lists
    for row in range(n):  # Loop through each row
        solutions = place_queen(row, n, solutions)  # Place a queen in each row and update solutions
    return solutions


def place_queen(row, n, prev_solutions):
    """Place a queen in a given row and return a list of updated solutions"""
    new_solutions = []  # Initialize new solutions as an empty list
    for solution in prev_solutions:  # Loop through each previous solution
        for col in range(n):  # Loop through each column
            if is_safe(row, col, solution):  # Check if the position is safe
                new_solutions.append(solution + [col])  # Add the position to the solution and append it to new solutions
    return new_solutions


def is_safe(row, col, solution):
    """Check if a position is safe for placing a queen"""
    if col in solution:  # Check if the column is already occupied
        return False
    else:
        # Check if the position is on the same diagonal as any of the previous queens
        return all(abs(solution[prev_row] - col) != row - prev_row
                   for prev_row in range(row))


def get_input():
    """Get the input from the command line and return it as an integer"""
    if len(sys.argv) != 2:  # Check if the number of arguments is correct
        print_error("Usage: nqueens N")  # Print the usage message
    else:
        try:
            n = int(sys.argv[1])  # Try to convert the argument to an integer
            return n
        except ValueError:  # Catch the exception if the argument is not a valid integer
            print_error("N must be a number")  # Print the error message


def validate_input(n):
    """Validate the input and return True if it is valid, False otherwise"""
    if n < 4:  # Check if the input is at least 4
        print_error("N must be at least 4")  # Print the error message
        return False
    else:
        return True


def print_error(message):
    """Print an error message and exit the program"""
    print(message)  # Print the message
    sys.exit(1)  # Exit with status code 1


def n_queens():
    """Main function that prints all the solutions for placing n queens on an n x n chessboard"""
    n = get_input()  # Get the input
    if validate_input(n):  # Validate the input
        solutions = generate_solutions(n)  # Generate all solutions
        for solution in solutions:  # Loop through each solution
            formatted_solution = []  # Initialize formatted solution as an empty list
            for row, col in enumerate(solution):  # Loop through each row and column
                formatted_solution.append([row, col])  # Format the position as a list of row and column
            print(formatted_solution)  # Print the formatted solution


if __name__ == '__main__':
    n_queens()  # Call the main function
