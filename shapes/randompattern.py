import turtle
from turtle import *
import random


pencil = turtle.Turtle()
steps = 100

while True:
    pencil.goto(random.random(),random.random())
    pencil.pendown()
   
    angles = random.randint(0, 360)
    pencil.forward(steps)
    pencil.left(angles)
    steps = steps + 10
    pencil.pencolor(random.random(), random.random(), random.random())
