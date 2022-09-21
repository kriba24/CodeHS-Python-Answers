speed(0)
penup()
setposition(-200,-200)
def draw_square():
    for i in range(4):
        pendown()
        forward(40)
        left(90)
draw_square()
for i in range(10):
    forward(40)
    draw_square()
left(90)

def square_lane():
    for i in range(10):
        forward(40)
        draw_square() 
for i in range(3):
    square_lane()
    left(90)