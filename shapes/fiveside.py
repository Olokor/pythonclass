import turtle
from turtle import *

pencil = turtle.Turtle()
pencil.penup()
pencil.goto(0,0)
pencil.pendown()

for numberofrepeat in range(5):
    pencil.forward(150)
    pencil.left(72)


turtle.mainloop()