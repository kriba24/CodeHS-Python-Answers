# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):

        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

# Your code here...
my_grid = []
for row in range(8):
    my_grid.append([0] * 8)

for row in range(3):
    for col in range(8):
        if (row + col) % 2 == 1:
            my_grid[row][col] = 1
for row in range(5,8):
    for col in range(8):
        if (row + col) % 2 == 1:
            my_grid[row][col] = 1
print_board(my_grid)