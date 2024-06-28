from turtle import Turtle
import random

# Class food herda de turtle
class Food(Turtle):
    # Tudo isso vai acontecer assim que um objeto food for criado
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Modifica o tamanho do objeto, o valor é multiplicado pelo valor inserido na funcao
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)