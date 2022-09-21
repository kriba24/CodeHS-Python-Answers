speed(0)
row_value = 0
radius = 25
numCircles = int(input("How many circles on the bottom row? "))
def move_to_row(numCircles):
    xValue = -((numCircles*50)/2)
    yValue = -200+(50*row_value)
    penup()
    setposition(xValue,yValue)
    pendown()
def circleRow(numCircles):
    for i in range(numCircles):
        circle(radius)
        penup()
        forward(radius*2)
        pendown()
for i in range(numCircles):
    move_to_row(numCircles)
    row_value = row_value + 1
    circleRow(numCircles)
    numCircles = numCircles - 1