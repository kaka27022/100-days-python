from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        #self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        """ Move the turtle up """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def down(self):
        """ Move the turtle down """
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def level_passed(self):
        """ Return the turtle to the starting position if the level was passed """
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False
    