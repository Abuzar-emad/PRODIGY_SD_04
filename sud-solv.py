# ("Sudoku Solver")

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

board = [
    [3, 1, 5, 0, 9, 7, 4, 0, 0],
    [4, 2, 0, 3, 0, 0, 0, 7, 0],
    [7, 0, 8, 0, 6, 0, 3, 0, 0],
    [0, 6, 4, 0, 2, 9, 0, 0, 0],
    [8, 3, 9, 0, 7, 4, 0, 0, 2],
    [0, 7, 2, 1, 0, 0, 0, 9, 0],
    [0, 0, 0, 9, 1, 0, 5, 8, 0],
    [0, 5, 0, 0, 8, 3, 9, 0, 0],
    [0, 8, 1, 0, 4, 5, 2, 3, 6]
]

print("Original Sudoku puzzle:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku puzzle:")
    print_board(board)
else:
    print("\nNo solution exists.")
