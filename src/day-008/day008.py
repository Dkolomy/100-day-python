# def greet():
#   print("Hello")
#   print("How are you?")
#   print("Isn't the weather nice today?")

# Positional Arguments
def greet_with_name(name, location):
  print(f"Hello {name} from {location}?")
  print(f"How are you {name}?")
  print(f"Isn't the weather nice today {name}?")

def life_in_weeks(age):
  print(f"You have {(90-age) * 52} weeks left.")

greet_with_name("John", "New York")
# Keyword Arguments
greet_with_name(location="New York", name="John")
life_in_weeks(20)