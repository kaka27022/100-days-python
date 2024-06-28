# Importa bibliotecas necessarias
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Jogador = Tartaruga
player = Player()
scoreboard = Scoreboard()

# Lista de carros
cars = []

# Sistema pra fazer a tartaruga andar pra frente quando pedido
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

# Flag auxiliar para surgimento dos carros
cont_cars = 0
cont_speed = 0

# Loop do jogo
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Aparece um novo carro a cada 6 loops
    if cont_cars == 6:
        cars.append(CarManager())
        cont_cars = 0
    
    cont_cars += 1

    # Checa se passou de nivel
    if player.level_passed():
        cont_speed += 1
        scoreboard.level += 1
        scoreboard.write_level()

    # Movimento de cada carro
    for car in cars:

        car.move_car(cont_speed)

        # Detecta se o carro bateu na tartaruga
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    
screen.exitonclick()
