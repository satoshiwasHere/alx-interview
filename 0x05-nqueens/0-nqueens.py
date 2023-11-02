#!/usr/bin/python3
"""
Program solving the N queens problem
The N queens puzzle is the challenge of placing N non-attacking,
queens on an N×N chessboard.
"""

import sys


def print_board(board):
    """
    This prints the game board
    """
    new_list = []
    for x, row in enumerate(board):
        value = []
        for y, col in enumerate(row):
            if col == 1:
                value.append(x)
                value.append(y)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, col, number):
    """
    This checks if placing 'number' at position (row, col),
    on the 'board' is safe
    """

    # Check this row in the left side
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check upper diagonal on left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, number, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def solveNQUtil(board, col, number):
    """
    Solves the N-Queens problem recursively for the 'board'
    & 'number' of queens placed so far
    """

    if (col == number):
        print_board(board)
        return True
    res = False
    for x in range(number):

        if (isSafe(board, x, col, number)):

            board[x][col] = 1

            res = solveNQUtil(board, col + 1, number) or res

            board[x][col] = 0

    return res


def solve(number):
    """
    Solves the N-Queens problem for a board of size 'number'
    """
    board = [[0 for x in range(number)]for x in range(number)]

    if not solveNQUtil(board, 0, number):
        return False

    return True


def validate(args):
    """
    Validates the given 'args' or arguments
    """
    if (len(args) == 2):
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """
    Main method for application execution
    """

    number = validate(sys.argv)
    solve(number)
