import turtle

pencil = turtle.Turtle()

turtle.bgcolor('#5FBF15')
turtle.tracer(10)

def star(pen, length):
    for numberofrepeat in range(5):
        if length <= 10:
            return pen.pendown()
        else:
            pen.forward(length)
            star(pencil, length/3)
            pen.left(216)

star(pencil, 300)
turtle.mainloop()