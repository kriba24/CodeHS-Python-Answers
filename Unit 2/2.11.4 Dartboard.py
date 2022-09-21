speed(0)
radius = 25
def move_to_next():
    penup()
    right(90)
    forward(25)
    left(90)
    pendown()
for i in range(4):
    circle(radius)
    move_to_next()
    radius = radius + 25