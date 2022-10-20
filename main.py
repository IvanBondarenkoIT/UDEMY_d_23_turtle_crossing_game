import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars(level=scoreboard.score_calc)
    if player.ycor() > 280:
        scoreboard.refresh_score()
        player.reset()

    for car in car_manager.cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()
            screen.update()

screen.exitonclick()