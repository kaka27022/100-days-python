from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(1, 2)
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        y = random.randint(-250, 250)
        self.goto(300, y)
        self.current_speed = STARTING_MOVE_DISTANCE

    def move_car(self, speed):
        """ Move car """
        self.setheading(180)
        self.forward(self.current_speed + (MOVE_INCREMENT*speed))

        