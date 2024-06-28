# class score
# class boardGame
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def r_points(self):
        self.r_score += 1
        self.clear()
        self.write_score()

    def l_points(self):
        self.l_score += 1
        self.clear()
        self.write_score()
        
