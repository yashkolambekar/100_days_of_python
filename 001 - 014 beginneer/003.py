# Day 3, lack of motivation, feeling tired, but let's fucking goooo


##################################### ROLLERCOASTER
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))
# age = int(input("What is your age in years?"))
# photo = input("Do you want a photo? Y or N: ")
# global addedprice

# if (photo == "Y") or (photo == "y"):
#     addedprice = 3
# else:
#     addedprice = 0

# if height > 120:
#     if age < 12:
#         print(f"You have to pay {5 + addedprice}$")
#     elif age >= 12 and age <= 18:
#         print(f"You have to pay {8 + addedprice}$")
#     elif age > 18:
#         print(f"You have to pay {10 + addedprice}$")

# else:
#     print("You are shorter than the required height")


####################################### ODD OR EVEN
# print("Odd or Even");
# number = int(input("Enter your number: "))
# if number %  2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


####################################### BMI CALCULATOR ADVANCED
# height  = float(input("enter your height in m: "))
# weight  = float(input("enter your weight in kg: "))
# bmi = (weight/(height ** 2))

# if bmi <= 18.5:
#     print("You are underweight")
# elif bmi > 18.5 and bmi <= 25:
#     print("You have normal weight")
# elif bmi > 25 and bmi <= 30:
#     print("You are overweight")
# elif bmi > 30 and bmi <= 35:
#     print("You are obese")
# elif bmi > 35:
#     print("You are clinically obese")


####################################### LEAP YEAR CHECKER
# print("Leap year checker")
# year = int(input("year: "))

# if (year % 4 == 0) and (year % 100 != 0):
#     print("This is a leep year")
# elif (year % 100 == 0) and (year % 400 == 0):
#     print("This is a leep year (with special case)")
# else:
#     print("Not a leap year")


######################################## PIZZA ORDER SYSTUMMM
# print("Welcome to the Pizza order systummm")
# size = input("Please select your size, S, M or L: ")
# pepperoni = input("Do you want pepperoni? Y or N: ")
# cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if (size == "S") or (size == "s"):
#     if pepperoni == "Y":
#         bill += 17
#     else:
#         bill += 15
# elif (size == "M") or (size == "L"):
#     if size == "M":
#         bill += 20
#     elif size =="L":
#         bill += 25
#     if pepperoni == "Y":
#         bill += 3
# if cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")


######################################## LOVE CALCULATOR
# print("Systummm hang karne wala love calculator!")

# name_1 = input("Your name: ")
# name_2 = input("His/Her name: ")

# true = 0
# true += name_1.count("t")
# true += name_2.count("t")
# true += name_1.count("r")
# true += name_2.count("r")
# true += name_1.count("u")
# true += name_2.count("u")
# true += name_1.count("e")
# true += name_2.count("e")

# love = 0
# love += name_1.count("l")
# love += name_2.count("l")
# love += name_1.count("o")
# love += name_2.count("o")
# love += name_1.count("v")
# love += name_2.count("v")
# love += name_1.count("e")
# love += name_2.count("e")

# final_points = (true * 10) + love

# print(f"Your final love score is {final_points}")


######################################## TREASURE ISLAND GAME

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to the Systumm Jam Game")

# print("You are on a road, there are two ways.")
# left_or_right = input("Where do you want to go, left or right? R or L: ")
# if left_or_right == "R":
#     print("Game Over")
#     exit()

# print("Now there is a river, you probably have to swim to go ahead")
# swim_or_wait = input("Do you want to swim or wait? S or W: ")
# if swim_or_wait == "S":
#     print("Game Over")
#     exit()

# print("Woah, it looks like you have reached!")
# which_door = input("Which door you want to open Red or Blue or Yellow? R or B or Y: ")
# if (which_door == "R") or (which_door == "B"):
#     print("Game Over")
#     exit()
# else:
#     print("You won, systum hang kar diya bhaii")

# Done!
# Jay Shree Ram