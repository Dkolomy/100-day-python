import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty = difficulty.lower()
attempts = 0
number = random.randint(1, 100)
if difficulty != "easy" and difficulty != "hard":
  print("Invalid difficulty. Please try again.")
else:
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5

  while attempts > 0:
    guess = int(input("Guess a number: "))
    if guess == number:
      print("You guessed the number! You win!")
      break
    else:
      if guess > number:
        print("Too high.")
      elif guess < number:
        print("Too low.")
      attempts -= 1
      print(f"You have {attempts} attempts left.")

  if attempts == 0:
    print("You ran out of attempts. You lose!")