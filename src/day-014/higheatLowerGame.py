# https://github.com/orgs/appbrewery/repositories

import random
from game_data import data

# Display art
print("----------------------------------")
score = 0
game_should_continue = True
account_b = random.choice(data)

def check_guess(guess, a, b):
  if a > b:
    return guess == 'a'
  else:
    return guess == 'b'

while game_should_continue:
  # Generate a random account from game data
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  # Format the account into a printable format
  print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
  print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

  # Ask user for guess
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct
  ## Get follower count of each account
  follower_count_a = account_a['follower_count']
  follower_count_b = account_b['follower_count']

  ## Use if statement to check if user is correct
  is_correct = check_guess(user_guess, follower_count_a, follower_count_b)

  # Give user feedback on their guess
  # score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_should_continue = False

# Make the game repeatable

# Making account at position B become the next account at position A

