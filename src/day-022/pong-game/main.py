# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score
# Game over

from tkinter import TclError
from turtle import Screen
from paddle import RightPaddle, LeftPaddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = RightPaddle()
left_paddle = LeftPaddle()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True


def close_game():
    global game_is_on
    game_is_on = False


def screen_is_open():
    try:
        return screen.getcanvas().winfo_exists()
    except TclError:
        return False


screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", close_game)

while game_is_on and screen_is_open():
    try:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (
            ball.distance(right_paddle) < 50 and ball.xcor() > 320
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320
        ):
            ball.bounce_x()

        # Detect when paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_score += 1
            scoreboard.update_scoreboard()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.right_score += 1
            scoreboard.update_scoreboard()
    except TclError:
        break

try:
    if screen_is_open():
        screen.bye()
except TclError:
    pass
