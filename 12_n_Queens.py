def isSafe(board,row,col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(row,board,n):
    if row == n:
        print("\nRoom Allicatoins:")
        for i in range(n):
            row = " ".join(["Q" if board[i] == j else "*" for j in range(n)])
            print(row)
        return True
    
    for col in range(n):
        if isSafe(board,row,col):
            board[row] = col
            if solve_n_queens(row +1 , board , n):
                return True
    return False

def allocate_rooms(n):
    board = [-1] * n
    if not solve_n_queens(0,board,n):
        print("no valid allocation possibe.")
    
try:
    N= int(input("Enter number of queens: "))
    if N <= 0:
        print("Enter a positive number.")
    else:
        allocate_rooms(N)
except ValueError:
    print("Invalid input . please enter a valid integer")