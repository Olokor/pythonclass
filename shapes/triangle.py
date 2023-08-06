# import turtle
# from turtle import *

# speed(1)
# bgcolor('blue')
# penup()
# goto(-150, -100)
# fillcolor('yellow')
# begin_fill()


# for number_of_repeat in range(3):
#     forward(300)
#     left(120)

# end_fill()

# # hideturtle()
# turtle.mainloop()

import turtle

# Create a Turtle instance
my_turtle = turtle.Turtle()

# Draw a rhombus
side_length = 100  # Length of each side of the rhombus

# Move turtle to starting position
my_turtle.penup()
my_turtle.goto(-side_length / 2, 0)  # Start at the left side of the rhombus
my_turtle.pendown()

# Draw the rhombus
for _ in range(2):  # Repeat the following instructions twice to draw two sides of the rhombus
    my_turtle.forward(side_length)
    my_turtle.left(60)
    my_turtle.forward(side_length)
    my_turtle.left(120)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()
