from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
