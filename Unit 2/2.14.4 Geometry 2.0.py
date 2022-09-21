speed(0)
radius = 20
penup()
setposition(0,-150)
pendown()
for i in range(7):
    circle(radius,360,i)
    radius = radius + 20