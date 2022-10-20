from turtle import Turtle
from car import Car
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
QTY_CARS = 15


class CarManager():
    def __init__(self):
        self.cars = []
        #self.spawn_coords_range = (-280, 280)
        for car in range(QTY_CARS):
            self.add_car()
        #self.spawn_coords_range = (280, 380)

    def add_car(self):
        rnd_position_y = random.randint(-260, 280)
        #rnd_position_x = random.randint(self.spawn_coords_range[0], self.spawn_coords_range[1])
        rnd_position_x = random.randint(-280, 280)
        new_car = Car((rnd_position_x, rnd_position_y), (random.choice(COLORS)))
        self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            if car.xcor() < -280:
                self.reset_car(car)
            else:
                speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level)
                car.goto(car.xcor() - speed, car.ycor())

    def reset_car(self, car):
        # self.cars.remove(car)
        # self.add_car()
        car.goto(280, random.randint(-280, 280))