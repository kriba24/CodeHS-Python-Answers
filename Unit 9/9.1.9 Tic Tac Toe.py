grid = ["0", "1","2","3","4","5","6","7","8","9"]
def board():
    print(grid[1] + " | " + grid[2] + " | " + grid[3] )
    print(grid[4] + " | " + grid[5] + " | " + grid[6] )
    print(grid[7] + " | " + grid[8] + " | " + grid[9] )

def placeMark(choice,mark):
    if choice == 1 and grid[1] == "1":
        grid[1] = mark
    elif choice == 2 and grid[2] == "2":
        grid[2] = mark
    elif choice == 3 and grid[3] == "3":
        grid[3] = mark
    elif choice == 4 and grid[4] == "4":
        grid[4] = mark
    elif choice == 5 and grid[5] == "5":
        grid[5] = mark
    elif choice == 6 and grid[6] == "6":
        grid[6] = mark
    elif choice == 7 and grid[7] == "7":
        grid[7] = mark
    elif choice == 8 and grid[8] == "8":
        grid[8] = mark
    elif choice == 9 and grid[9] == "9":
        grid[9] = mark
    else:
        print("Invalid Move.")
    board()
def checkWinner(i):
    if grid[1] == grid[2] and grid[2] == grid[3]:
        return 1 
    elif grid[4] == grid[5] and grid[5] == grid[6]:
        return 1
    elif grid[7] == grid[8] and grid[8] == grid[9]:
        return 1
    elif grid[1] == grid[4] and grid[4] == grid[7]:
        return 1
    elif grid[2] == grid[5] and grid[5] == grid[8]:
        return 1 
    elif grid[3] == grid[6] and grid[6] == grid[9]:
        return 1
    elif grid[1] == grid[5] and grid[5] == grid[9]:
        return 1
    elif grid[3] == grid[5] and grid[5] == grid[7]:
        return 1
    elif grid[1]!= "1" and grid[2]!= "2"  and grid[3]!= "3"\
    and grid[4]!= "4" and grid[5]!= "5"  and grid[6]!= "6"\
    and grid[7]!= "7" and grid[8]!= "8"  and grid[9]!= "9":
        return 0 
    else:
        return -1
board()
i = -1 
playerNum = 1 
while i == -1: 
    print("Player " + str(playerNum)+ ": " )
    try:
        choice = int(input("Choose a number to place your X or O"))
        if playerNum == 1:
            mark = "X"
        else: 
            mark = "O"
        placeMark(choice,mark) 
        i = 1 
    except ValueError:
        print("Enter an integer")
    i = checkWinner(i)
    if playerNum == 1:
        playerNum = 2 
    else:
        playerNum = 1 
if i == 0:
    print("draw")
elif i == 1 and mark == "X":
    print("player 1 wins!!")
else:
    print("player 2 wins!!")