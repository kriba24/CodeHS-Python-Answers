speed(0)
def beaded_bracelet():
    penup()
    forward(100)
    pendown()
    circle(10)
    penup()
    backward(100)
    left(10)
for i in range(36):
    beaded_bracelet()