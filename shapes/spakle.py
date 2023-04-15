import turtle 
from turtle import *
import random

pencil = turtle.Turtle()

steps = 0
# pencil.pensize(100)
pencil.penup()
pencil.goto(0,0)
turtle.bgcolor('#000000')
pencil.pendown()

pencil.speed(300)

for numberofrepeat in range(249):
    pencil.forward(steps)
    pencil.left(169)
    steps +=1
    pencil.pencolor(random.random(), random.random(), random.random())

turtle.mainloop()