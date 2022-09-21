speed(0)
penup()
setposition(-150,0)
pendown()
length = 10
def draw_square():
    for i in range(4):
        forward(length)
        left(90)
for i in range(4):
    draw_square()
    penup()
    forward(length * 2)
    length = (length+10)
    pendown()