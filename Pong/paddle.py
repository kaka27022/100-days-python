from turtle import Turtle
# Create and move a paddle
# class players
MOVE = 20

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shapesize(5, 1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
    
    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)
        