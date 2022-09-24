def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))
board = []
for i in range(8):
    board.append([0] * 8)
for row in range(3):
    for col in range(8):
        board[row][col] = 1
for row in range(5,8):
    for col in range(8):
        board[row][col] = 1
print_board(board)