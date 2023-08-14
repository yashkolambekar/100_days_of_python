########################################################### IMPORTING TURTLE

# from turtle import Turtle, Screen
# import random

# timmy = Turtle()

# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.color("DarkRed")
# for i in range(50):
#     if i % 2 == 0:
#         timmy.left(random.randint(45, 90))
#     else:
#         timmy.right(random.randint(45, 90))
#     timmy.forward(random.randint(1, 10))
# my_screen.exitonclick()


########################################################### PRETTY TABLE

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)