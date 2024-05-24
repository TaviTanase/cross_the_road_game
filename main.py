import time
from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = Car_manager()
scoreboard = Scoreboard()
screen.onkey(player.move,"Up")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.cars[1:len(car_manager.cars)]:
        if player.distance(car)<28:
            game_is_on=False
            time.sleep(0.5)
            screen.clear()
            scoreboard.gameover()

    if player.ycor()>280:
        player.reset()
        scoreboard.update()
        car_manager.update()




screen.exitonclick()