speed(10)
penup()
color("gray")
setposition(0,-200)
def draw_circle(radius):
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius*2)
    right(90)
bottom_radius = int(input("What should the radius be?: "))
for i in range(3):
    draw_circle(bottom_radius)
    bottom_radius = bottom_radius/2