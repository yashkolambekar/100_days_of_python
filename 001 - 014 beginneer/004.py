# Day 4, let's go baby!!!
# Enigmaaaaaaaaaa, rule no 1, don't fuck with the Gs


################################### Python Random Module
import random

# random_integer = random.randint(a, b)
# random_float = random.random()
# random_between_0_and_5 = (random.random()) + (random.randint(0, 4))
# random_between_0_and_5 = (random.random() * 5)


################################### HEADS OR TAILS
# random_number = random.random()

# if random_number > 0.5:
#     print("Heads")
# else:
#     print("Tails")


#################################### PYTHON LIST
# List in python is same as Array in Javascript, not much of a difference 
# states = ["Maharashtra", "Gujarat", "Uttarakhand", "Uttar Pradesh", "Assam", "Manipur"]
# print(states[0])


#################################### BILL BOWL CHALLENGE (LONDON ROULETTE)
# print("Welcome to the Bill payer chooser game!\n")
# names_raw_string = input("Give a list of names seperated bya Comma and a space (', '): ")
# names = names_raw_string.split(", ")

# random_number = random.randint(0, len(names) - 1)
# print(random_number)
# print(f"{names[random_number]} is going to pay the bill today!")


#################################### ROCK, PAPERS and SCISSORS GAME

# pictures = [
#     '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''',
# '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''',
# '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# ]
# moves = ["Rock", "Papers", "Scissors"]
# computer_move = random.randint(0, len(moves) - 1)

# player_move_raw = input("Choose your move (R, P or S): ")

# global player_move
# if player_move_raw == "R":
#     player_move = 0
# elif player_move_raw == "P":
#     player_move = 1
# elif player_move_raw == "S":
#     player_move = 2
# else:
#     print("enter something valid")
#     exit()

# print(f"You chose: \n {pictures[player_move]}")
# print(f"Computer chose: \n {pictures[computer_move]}")

# if player_move == computer_move:
#     print("Its a draw!")
# elif (player_move == 0 and computer_move == 2) or (player_move == 1 and computer_move == 0) or (player_move == 2 and computer_move == 1):
#     print("You won!")
# elif (player_move == 2 and computer_move == 0) or (player_move == 0 and computer_move == 1) or (player_move == 1 and computer_move == 2):
#     print("Computer won!") 


# Day 4 done (on day 5 though)