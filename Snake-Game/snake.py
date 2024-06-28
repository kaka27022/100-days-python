from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    # Step 1 - Create the snake body
    ## Inicializa o corpo da cobra
    def __init__(self):
        self.snake_list = []
        self.x = 0
        self.create_snake()

    def create_snake(self):
        # Cobra inicial - 3 turtles
        ## Criando 3 objetos para ser o inicio da cobra
        ## Tentar colocar separado em metodos em vez de na iniciacao
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        snake_initial = Turtle("square")
        snake_initial.color("white")
        snake_initial.penup()
        snake_initial.goto(position)
        self.snake_list.append(snake_initial)

    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000, 1000)
        self.snake_list.clear()
        self.x = 0
        self.create_snake()
    
    def extend(self):
        # Aumenta a cobra
        ## Lembrar que tem como pegar a ultima posicao de uma lista atraves de numeros negativos
        self.add_segment(self.snake_list[-1].position())
    
    # Faz todos os movimentos da cobra
    def move(self):
        # For que move de tras pra frente
        ## For para fazer com que cada parte da cobra de mova pra parte da frente
        ## Assim a movimentacao vai ser continua e so vai precisar mover a primeira parte da cobra sempre
        for seg_num in range(len(self.snake_list) - 1, 0,-1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)

        self.snake_list[0].forward(MOVE_DISTANCE)
    
    def up(self):
        # So precisa mover a cabeca da cobra pq o resto do corpo segue a cabeca
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)
    
    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)
    
    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    