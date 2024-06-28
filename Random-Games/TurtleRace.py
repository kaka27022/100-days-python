from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()
color = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtle(turtle_number):
    turtle = Turtle("turtle")
    turtle.color(color[turtle_number])
    turtle.penup()
    turtle.goto(x=-230, y=-75 + (turtle_number * 30))
    return turtle

turtles = []

for turtle_index in range(6):
    turtles.append(create_turtle(turtle_index))

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")
            #screen.bye()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.bye()