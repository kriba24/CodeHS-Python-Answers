speed(10)
penup()
setposition(0,-100)
radius = 100
for i in range(4):
    pendown()
    begin_fill()
    color_choice = input("What color should this circle be?: ")
    color(color_choice)
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(25)
    right(90)
    radius = radius-25