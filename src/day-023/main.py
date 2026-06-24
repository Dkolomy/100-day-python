# Move the turtle with keypress
# Create a turtle race game
# Detect collision with car
# Detect when turtle reaches the other side
# Create a scoreboard

from turtle import Turtle, Screen
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()