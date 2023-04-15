import turtle

pencil = turtle.Turtle()

def circle():
    pencil.pendown
    for numberofrepeat in range(360):
        pencil.forward(1)
        pencil.left(1)

def square():
    pencil.pendown()
    for numberofrepeat in range(4):
        pencil.forward(100)
        pencil.left(90)

def triangle():
    pencil.pendown
    for numberofrepeat in range(3):
        pencil.forward(100)
        pencil.left(120)

pencil.penup()
pencil.goto(-171, 14)
pencil.pendown()
circle()
pencil.penup()
pencil.goto(31, 39)
pencil.pendown()
circle()
pencil.penup()
pencil.goto(129, -35)
pencil.pendown
triangle()
pencil.penup()
pencil.goto(-153, -70)
pencil.down()
triangle()


