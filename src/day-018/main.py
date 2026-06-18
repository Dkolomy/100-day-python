from turtle import Turtle, Screen
import random
# import heroes

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

from turtle import colormode
colormode(255)
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

def draw_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

timmy_the_turtle.speed("fastest")

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

# print(heroes.gen())