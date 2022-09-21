speed(10)
penup()
setposition(-150,0)
def make_square(length):
    if length % 2 == 0:
        begin_fill()
        color("black")
    for i in range(4):
        pendown()
        forward(25)
        left(90)
    end_fill()
        
for i in range(6):
    make_square(i)
    penup()
    forward(50)