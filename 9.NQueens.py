
def print_board(board, n):
    print("\nSolution:")
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def is_safe(board, row, col):
    # Check all previously placed queens
    for i in range(row):
        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queen(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    # Try every column in the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            # Place queen in the next row
            if solve_n_queen(board, row + 1, n):
                return True

            # Backtrack: remove the queen
            board[row] = -1

    return False


n = int(input("Enter the value of N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    board = [-1] * n

    if solve_n_queen(board, 0, n):
        print_board(board, n)
    else:
        print("No solution exists for N =", n)
