from turtle import Turtle



class Car(Turtle):
    def __init__(self, position, color):
        super(Car, self).__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.goto(position)
        self.penup()
        self.shapesize(stretch_len=2.5, stretch_wid=1)

