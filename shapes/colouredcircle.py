import turtle 
from turtle import *
import random

pencil = turtle.Turtle()
pencil.pendown()
pencil.speed(300)

for numberofrepeat in range(100):
    pencil.forward(150)
    pencil.left(93)
    pencil.pencolor(random.random(), random.random(), random.random())

turtle.mainloop()

