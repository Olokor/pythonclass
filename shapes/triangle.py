import turtle
from turtle import *

speed(1)
bgcolor('blue')
penup()
goto(-150, -100)
fillcolor('yellow')
begin_fill()


for number_of_repeat in range(3):
    forward(300)
    left(120)

end_fill()

# hideturtle()
turtle.mainloop()