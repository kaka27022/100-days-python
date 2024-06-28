from turtle import Screen
# Class player
from paddle import Paddle
# Class Ball
from ball import Ball
import time
# class score
# class boardGame
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle(350, 0)
# Create another paddle
l_paddle = Paddle(-350, 0)

# Create the ball and make it move
ball = Ball()
# Keep score
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

flag_up = True
game_is_on = True

while game_is_on: 
    time.sleep(ball.ball_speed)
    screen.update()
    
    # Switch moviment of the ball
    if flag_up:
        ball.move()
    else:
        ball.bounce_y()

    # Detect collision with wall and bounce
    if ball.ycor() > 280:
        flag_up = False
    if ball.ycor() < -280:
        flag_up = True

    # Detect collision with paddle
    # Poderia ter colocado l e f em um mesmo if
    ## Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    ## Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
     
    # Detect when paddle misses
    ## Detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_points()
    ## Detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_points()

screen.exitonclick()