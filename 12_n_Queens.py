def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row, board, n):
    if row == n:
        print("\nRoom Allocations:")
        for i in range(n):
            line = ""
            for j in range(n):
                line+=" Q " if board[i] == j else " * "
            print(line.strip())
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve(row + 1, board, n):
                return True
    return False

def allocate_rooms(n):
    board = [-1] * n
    if not solve(0, board, n):
        print("No valid allocation possible.")

try:
    N = int(input("Enter number of queens: "))
    if N > 0:
        allocate_rooms(N)
    else:
        print("Enter a positive number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
