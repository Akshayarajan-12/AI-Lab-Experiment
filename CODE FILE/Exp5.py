N = 8

# Create an 8 x 8 chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

# Store the column position of each queen
positions = []

# Count placement attempts
attempts = 0


def is_safe(row, col):
    # Check the same column in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    global attempts

    # All eight queens have been placed
    if row == N:
        return True

    # Try placing a queen in each column
    for col in range(N):
        attempts += 1

        if is_safe(row, col):
            # Place the queen
            board[row][col] = 1
            positions.append((row + 1, col + 1))

            # Solve the next row recursively
            if solve(row + 1):
                return True

            # Backtrack: remove the queen
            board[row][col] = 0
            positions.pop()

    return False


# Execute the algorithm
if solve(0):
    print("Valid 8-Queens Solution:\n")

    # Display the chessboard
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

    print("\nQueen Positions (Row, Column):")
    for position in positions:
        print(position)

    print("\nTotal placement attempts:", attempts)
else:
    print("No solution exists.")