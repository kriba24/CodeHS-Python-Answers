speed(0)
def row():
    color_value = 1
    for i in range(10):
        if color_value % 2 == 0:
            color("black")
        else:
            color("red")
        begin_fill()
        for j in range(4):
            forward(40)
            left(90)
        end_fill()
        penup()
        forward(40)
        pendown()
        color_value = color_value + 1
def next_row():
    penup()
    left(90)
    forward(80)
    left(90)
    pendown()
penup()
setposition(-200,-200)
pendown()
for i in range(5):
    row()
    next_row()
    row()
    right(180)