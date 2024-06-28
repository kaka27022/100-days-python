from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_counter_clock():
    tim.left(10)

def turn_clock():
    tim.right(10)

def clear():
    screen.resetscreen()

screen.listen()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = turn_counter_clock)
screen.onkey(key = "d", fun = turn_clock)
screen.onkey(key = "c", fun = clear)

screen.exitonclick()