speed(0)
penup()
setposition(0,150)
def draw_circle():
    circle(25)
def draw_square():
    for i in range(4):
        forward(50)
        left(90)
pendown()
for i in range(4):
    draw_circle()
    right(90)
    penup()
    forward(100)
    left(90)
    pendown()
penup()
setposition(-25,-200)
pendown()
for i in range(4):
    draw_square()
    penup()
    right(90)
    backward(100)
    left(90)
    pendown()