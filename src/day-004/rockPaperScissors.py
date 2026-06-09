import random

rock = """
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
"""

paper = """
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
"""

scissors = """
          _______
      ---'   ____)____
                ______)
             __________)
              (____)
      ---.__(___)
"""

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0(rock), 1(paper), 2(scissors). "))
computer_choice = random.randint(0, 2)

print(f"You chose {game_images[user_choice]}")
print(f"Computer chose {game_images[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")