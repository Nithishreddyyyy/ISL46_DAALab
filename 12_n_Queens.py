def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(row, board, n):
    if row == n:
        print("\nRoom allocation (Q = Queen):")
        for r_idx in range(n):
            row_str = " ".join(["Q" if board[r_idx] == c_idx else "*" for c_idx in range(n)])
            print(row_str)
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(row + 1, board, n):
                return True 
    return False

def allocate_rooms(n):
    board = [-1] * n
    if not solve_n_queens(0, board, n):
        print("No valid allocation possible.")

# --- Main execution ---
try:
    N = int(input("Enter number of Queens: "))
    if N <= 0:
        print("Please enter a positive integer for the number of Queens.")
    else:
        allocate_rooms(N)
except ValueError:
    print("Invalid input. Please enter an integer.")