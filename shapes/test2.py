import turtle

pencil = turtle.Turtle()

def circle(pen, radius):
    pen.pendown()
    for numberofrepeat in range(360):
        pen.forward(radius)
        pen.left(1)

def square(pen, length):
    pen.pendown()
    for numberofrepeat in range(4):
        pen.forward(length)
        pen.left(90)

length = float(input("enter the value for length of the square: "))
square(pencil, length)



radius = float(input("enter the value for radius: "))
pencil.penup()
pencil.goto(129, -53)
pencil.pendown()
circle(pencil, radius)