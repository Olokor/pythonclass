import turtle

pencil = turtle.Turtle()
turtle.tracer(10)

pencil.speed(0)
turtle.bgcolor("black")

# colours = ["yellow", "red", "yellow", "red"]
colours = ["#6C45B0", "#5EB045", "#B04545", "#152E05"]

for i in range(120):

    for colour in colours:
        pencil.pencolor(colour)
        pencil.circle(200-i, 100)
        pencil.left(90)
        pencil.circle(200-i, 100)
        pencil.right(60)

turtle.mainloop()




