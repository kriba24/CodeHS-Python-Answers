speed(0)
import random
secret_number = random.randint(1,10)
print(secret_number)
user_number = int(input("Type a number between 1 and 10: "))
def check_mark():
    pensize(15)
    color("green")
    right(45)
    backward(50)
    forward(50)
    left(90)
    forward(100)
def down_arrow():
    pensize(15)
    penup()
    setposition(0,100)
    pendown()
    right(90)
    forward(100)
    left(135)
    forward(25)
    backward(25)
    left(90)
    forward(25)
    penup()
    setposition(0,0)
    right(135)
    pendown()
def up_arrow():
    pensize(15)
    penup()
    setposition(0,-100)
    pendown()
    left(90)
    forward(100)
    left(135)
    forward(25)
    backward(25)
    left(90)
    forward(25)
    penup()
    setposition(0,0)
    left(45)
    pendown()
while user_number != secret_number:
    if user_number > secret_number:
        up_arrow()
        user_number = int(input("Sorry! Try again. Type a number between 1 and 10: "))
        clear()
        penup()
        setposition(0,0)
        pendown()
    else:
        down_arrow()
        user_number = int(input("Sorry! Try again. Type a number between 1 and 10: "))
        clear()
        penup()
        setposition(0,0)
        pendown()
check_mark()