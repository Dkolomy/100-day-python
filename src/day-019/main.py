from turtle import Turtle, Screen
import random

def move_forward():
    timmy_the_turtle.forward(10)

def move_backward():
    timmy_the_turtle.backward(10)

def move_counter_clockwise():
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)

def move_clockwise():
    timmy_the_turtle.setheading(timmy_the_turtle.heading() - 10)

def clear_screen():
    timmy_the_turtle.clear()
    timmy_the_turtle.penup()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()

timmy_the_turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)

screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()