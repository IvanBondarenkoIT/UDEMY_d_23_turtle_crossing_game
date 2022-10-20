from turtle import Turtle
ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score_calc = -1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align="center", font=FONT)

    def refresh_score(self):
        self.score_calc += 1
        # CAR SPEED UP
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.score_calc}", True, align=ALIGN, font=FONT)
