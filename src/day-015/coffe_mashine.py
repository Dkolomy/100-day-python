# Print report
# Check resources sufficient
# Process coins
# Check transaction successful
# Make coffee

MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  },
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
  "money": 0,
}

# TODO: 1. Print report
def print_report():
  """Prints the current state of the coffee machine."""
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${resources['money']}")

# TODO: 2. Check resources sufficient
def is_resource_sufficient(order_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

# TODO: 3. Process coins
def process_coins(cost):
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  total = int(input("How many quarters? ")) * 0.25
  total += int(input("How many dimes? ")) * 0.10
  total += int(input("How many nickels? ")) * 0.05
  total += int(input("How many pennies? ")) * 0.01
  return total

# TODO: 4. Check transaction successful
def is_transaction_successful(payment, cost):
  """Returns True when payment is greater than or equal to cost, False if not."""
  if payment >= cost:
    change = round(payment - cost, 2)
    print(f"Here is ${change} in change.")
    resources['money'] += cost
    return True
  else:
    return False

# TODO: 5. Make coffee
def make_coffee(drink_name, order_ingredients):
  """Deduct the required ingredients from the resources."""
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
while is_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print_report()
  else:
    drink = MENU[choice]
    if is_resource_sufficient(drink['ingredients']):
      payment = process_coins(drink['cost'])
      if is_transaction_successful(payment, drink['cost']):
        make_coffee(choice, drink['ingredients'])
      else:
        print("Sorry that's not enough money. Money refunded.")
    else:
      print("Sorry there is not enough ingredients.")
      