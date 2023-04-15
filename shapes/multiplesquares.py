import turtle
import random

pencil = turtle.Turtle()

def square(length):
    pencil.pendown()
    for numberofrepeat in range(4):
        pencil.forward(length)
        pencil.left(90)


def draw(length, x, y):
    pencil.penup()
    pencil.goto(x,y)
    square(length)


for numberofrepeat in range(5):
    x, y = random.randint(100, 200), random.randint(-200, 200)
    draw(random.randint(100, 250), x, y)

