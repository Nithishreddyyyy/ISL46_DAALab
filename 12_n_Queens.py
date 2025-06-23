def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(row, board, n):
    if row == n:
        print("\nRoom allocation (Q = Queen):")
        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        return True  # Only one solution needed

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve(row + 1, board, n):
                return True
    return False

def allocate_rooms(n):
    board = [-1] * n  # board[i] = column number where student is placed in row i
    if not solve(0, board, n):
        print("No valid allocation possible.")

# Run the program
N = int(input("Enter number of students / room size (N): "))
allocate_rooms(N)
