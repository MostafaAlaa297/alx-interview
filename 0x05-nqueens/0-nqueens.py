#!/usr/bin/python3
"""
0x05. N Queens
"""
import sys


def validate_args():
    """Validating args"""
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
        exit(1)

    return N

N = validate_args()

def is_safe(board, row, col):
    """
    checks if placing a queen
    at board[row][col] is safe by checking
    the row, upper diagonal,
    and lower diagonal on the left side
    """
    
    for i in range(col):
        if board[row][1] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    """Solves nqueesnds"""
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0
    return res

def print_solution(board):
    """Prints the board"""
    solution = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def nqueens():
    N = validate_args()
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    nqueens()
