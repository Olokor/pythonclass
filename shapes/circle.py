import turtle

turtle.tracer(10)
pencil = turtle.Turtle()
def circle(pen, radius):
    for numberofrepeat in range(360):
        pen.forward(radius)
        pen.left(1)

pencil.speed(0)
colours = ["#23685F", "#4E4998", "#08372B", "#180E5B", "#3D0404", "#3D0404", "#5D7713", "#179C86"]
for numberofrepeat in range(5):
    for color in colours:
        pencil.pencolor(color)
        circle(pencil, 1)
        pencil.left(10)

turtle.mainloop()