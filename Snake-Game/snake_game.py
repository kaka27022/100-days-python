from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
# Modifica o tamanho da tela
screen.setup(width=600, height=600)
# Troca a cor da tela
screen.bgcolor("black")
# Coloca um titulo na tela
screen.title("My Snake Game")
# So mostra o que foi feito na tela depois do update
screen.tracer(0)
# Step 1 - Create the snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Step 3 - Make the snake obey commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Step 2 - Make the snake move
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detectar colisao com a comida.
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detectar colisao com a parede
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -300 or snake.snake_list[0].ycor() > 300 or snake.snake_list[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    # Detectar colisao com a propria cobra
    # NOTA: Slice = Separar a lista em valores determinados: [2:5] -> Vai apenas da posicao 2 pra 5 da lista
    ## [1:] -> Tudo desde a posicao 1
    ## [:5] -> Tudo ate a posicao 5
    ## [2:5:2] -> Vai da posicao 2 para a 5 de 2 em 2
    ## [::2] -> Corre a lista de 2 em 2
    ## [::-1] -> Inverte a lista
    # Tambem pode ser usado em tuplas
    for segment in snake.snake_list[1:]:
        if snake.snake_list[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

scoreboard.file.close("data.txt")
screen.exitonclick() 