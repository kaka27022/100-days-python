from turtle import Turtle

# Ter o costume de sempre fazer constantes para escritas do codigo
ALIGN = "center"
FONT = ("Arial", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # Melhor usar o with pra ficar abrindo
        file = open("data.txt", mode = "r")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x = 0, y = 270)
        self.color("white")
        self.score = 0
        self.high_score = int(file.read())
        self.write_update()
    
    def write_update(self):
        self.clear()
        self.write(arg= f"Score: {self.score} High Score: {self.high_score}", move= False, align= ALIGN, font= FONT)

    #def game_over(self):
    #    self.goto(x = 0, y = 0)
    #    self.write(arg= "GAME OVER", move= False, align= ALIGN, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        file = open("data.txt", "w")
        file.write(str(self.high_score))
        self.score = 0
        self.write_update()

    def update_score(self):
        self.score += 1
        self.write_update()

    