import turtle 
import random

pencil = turtle.Turtle()


def square(pen, length):
    for numberofrepeat in range(4):
        pen.forward(length)
        pen.left(90)

for numberofrepeat in range(10):
    pencil.penup()
    pencil.goto(random.randint(-200, 200), random.randint(-200, 200))
    pencil.pendown()
    square(pencil, 100)
turtle.mainloop()