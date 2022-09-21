speed(10)
pensize(10)
rating = int(input("What is your rating?: "))
def x_mark():
    color("red")
    left(45)
    for i in range(4):
        forward(30)
        penup()
        backward(30)
        left(90)
        pendown()
def yellow_line():
    color("gold")
    penup()
    backward(30)
    pendown()
    forward(60)
def check_mark():
    color("green")
    right(45)
    backward(50)
    forward(50)
    left(90)
    forward(100)
if 1 <= rating <= 4:
    x_mark()
elif 5<= rating <= 7:
    yellow_line()
else:
    check_mark()