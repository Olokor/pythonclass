import turtle
pencil = turtle.Turtle()

class Draw:
    def __init__(self, length=None, radius=None) -> None:
        self.length = length
        self.radius = radius
    
    def square(self):
        for numberofrepeat in range(4):
            pencil.forward(self.length)
            pencil.left(90)
    
    def circle(self):
        turtle.tracer(10)
        for numberofrepeat in range(360):
            pencil.forward(self.radius)
            pencil.left(1)


draw = Draw(100, 1)
draw.circle()
draw.square()


            


