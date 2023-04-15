import turtle
from turtle import *
import random
pencil = turtle.Turtle()
pencil.penup()
length = 0 #length of my square
pencil.goto(0,0)
pencil.pendown()
pencil.speed(100)
for numberofrepeat in range(100):
    pencil.forward(length)
    length +=5
    pencil.left(90)
    pencil.pencolor(random.random(), random.random(), random.random())

turtle.mainloop()