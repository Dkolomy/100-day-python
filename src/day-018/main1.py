from turtle import Turtle, Screen
import random
# import heroes

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a dashed line
# Position on the left side of the screen
# timmy_the_turtle.penup()
# timmy_the_turtle.goto(-200, 0)
# timmy_the_turtle.pendown()
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# timmy_the_turtle.penup()
# timmy_the_turtle.goto(-100, 100)
# timmy_the_turtle.pendown()

# https://trinket.io/docs/colors
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen"]

# for i in range(3, 11):
#   num_sides = i
#   timmy_the_turtle.color(random.choice(colors))
#   angle = 360 / num_sides
#   for _ in range(num_sides):
#       timmy_the_turtle.forward(100)
#       timmy_the_turtle.right(angle)

from turtle import colormode
colormode(255)
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

directions = [0, 90, 180, 270]
for _ in range(200):
  timmy_the_turtle.color(random_color())
  timmy_the_turtle.width(10)
  timmy_the_turtle.speed("fastest")
  timmy_the_turtle.forward(30)
  timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()

# print(heroes.gen())