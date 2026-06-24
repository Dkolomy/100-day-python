from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_len=1, stretch_wid=5)
    self.penup()
    self.goto(position) # position is a tuple (x, y)

  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

class RightPaddle(Paddle):
  def __init__(self):
    super().__init__((350, 0))

class LeftPaddle(Paddle):
  def __init__(self):
    super().__init__((-350, 0))