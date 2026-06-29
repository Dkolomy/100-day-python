def add(*args):
  return sum(args)

def show_args(*args):
  print(args[-1])
  for arg in args:
    print(f"arg: {arg}")

print(add(1, 2, 3, 4, 5))
show_args(1, 2, 3, 4, 5)

def calculate(n, **kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f"key: {key}, value: {value}")

  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)

class Car:
  def __init__(self, **kw):
    self.make = kw["make"]
    self.model = kw["model"]

  def show_car(self):
    print(f"Car: {self.make} {self.model}")

my_car = Car(make="Nissan", model="GT-R")
my_car.show_car()