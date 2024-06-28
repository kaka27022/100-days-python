from turtle import Turtle
# Create the ball and make it move
# class ball

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """ Move the ball up """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """ Switch the side off the ball moviment Y """
        # Outra forma seria multiplicar a cordenada Y por -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """ Switch the side off the ball moviment X """
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        """ Switch the side off the ball moviment X and starts from the beggining"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()