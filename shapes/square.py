import turtle
from turtle import *
 
pencil = turtle.Turtle()

pencil.speed(1)
pencil.penup()
pencil.goto(0,0)

pencil.pendown()

for number_of_repeat in range(4):
    pencil.forward(100)
    pencil.left(90)


pencil.down()
