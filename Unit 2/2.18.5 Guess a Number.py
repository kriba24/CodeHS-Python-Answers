def check_mark():
    pensize(15)
    color("green")
    right(45)
    backward(50)
    forward(50)
    left(90)
    forward(100)
secret_number = 4
user_number = int(input("Type a number between 1 and 10: "))
if user_number == secret_number:
    check_mark()