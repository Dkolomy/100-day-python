import turtle

class State(turtle.Turtle):
  def __init__(self, x, y, state):
    super().__init__()
    self.state = state
    self.hideturtle()
    self.penup()
    self.goto(x, y)
    self.write(self.state)