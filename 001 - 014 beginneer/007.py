# 3rd session of the day! Let's go

########################################################### HANG MAN GAME

import random
import os

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["yash", "sai", "siddhi", "aatish"]

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)

empty_answer_list = []
guessed_letters = len(chosen_word_list)
lives = 0; 

for i in chosen_word_list:
    empty_answer_list.append("_")

while guessed_letters:
    input_letter = input("Guess a letter: ")
    attempt_fail = True
    counter_1 = 0
    for char in chosen_word_list:
        if input_letter == char:
            empty_answer_list[counter_1] = char
            chosen_word_list[counter_1] = "__NONE__"
            guessed_letters -= 1
            attempt_fail = False
            break
        counter_1 += 1
    if attempt_fail:
        lives += 1

    if lives < 7:
        os.system("cls")
        print(stages[6 - lives])
        print(empty_answer_list)
    else:
        print("You lose")
        exit()

    

print("You WON!")


# Let's go DONE!