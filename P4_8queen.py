import numpy as np
import pandas as pd

def is_safe(board, row, col):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = np.zeros((n, n), dtype=int)
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
    else:
        print("Solution:")
        df = pd.DataFrame(board)
        print(df)

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

if __name__ == "__main__":
    n = 8
    solve_n_queens(n)
