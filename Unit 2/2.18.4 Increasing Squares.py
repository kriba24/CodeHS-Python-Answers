speed(0)
length = 50
def square():
    for i in range(4):
        forward(length)
        left(90)
while length <= 350:
    penup()
    setposition(-length/2,-length/2)
    pendown()
    square()
    length = length + 50