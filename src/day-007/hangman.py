# Hangman Game
import random
from hangman_words import word_list
from hangman_stages import stages

lives = len(stages) - 1
correct_letters = []

# TODO randomly choose a word
picked_word = random.choice(word_list)
# print(picked_word)
masked_word = '_' * len(picked_word)
print(masked_word)

user_ended_game = False

while not user_ended_game:
    user_letter_found = False
    masked_word_list = list[str](masked_word)
    print(f"You have {lives} lives left")
    user_letter = input("Enter a letter: ").lower()

    if user_letter not in correct_letters:
        correct_letters.append(user_letter)
    else:
        print(f"You have already guessed {user_letter}")
        continue

    for i in range(len(picked_word)):
      if picked_word[i] == user_letter:
        masked_word_list[i] = user_letter
        user_letter_found = True

    masked_word = ''.join(masked_word_list)
    print(masked_word)

    if not user_letter_found:
        lives -= 1
        print(f"You guessed wrong {user_letter}. You have {lives} lives left")
        if lives == 0:
            print(f"********** You lose! The word was {picked_word} **********")
            user_ended_game = True

    if masked_word.count('_') == 0:
        print("********** You win! **********")
        user_ended_game = True

    print(stages[lives])