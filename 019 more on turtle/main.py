from turtle import Turtle, Screen
import random

# tim = Turtle()
# screen = Screen()
# screen.listen()

########################################################### ETCH A SKETCH

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def move_right():
#     tim.right(90)

# def move_left():
#     tim.left(90)

# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="d", fun=move_right)
# screen.onkeypress(key="a", fun=move_left)


########################################################### TIMEPASS WITH TURTLE

# tim.speed("fastest")
# tim.speed("fastest")
# line_length = 0
# box_padding = 8

# for i in range(30):
#     for j in range(1):
#         tim.forward(line_length)
#         tim.right(90)
#     tim.left(90)
#     tim.forward(box_padding)
#     tim.right(90)
#     line_length += box_padding


########################################################### TURTLE RACE

import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")

turtle_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = [];
for i in range(7):
    turtles.append(Turtle())

itr = 0
y = 100
for t in turtles:
    t.shape("turtle")
    t.penup()
    t.color(turtle_colors[itr])
    t.goto(x=-230, y=y)
    y -= 30
    itr += 1

winner = ""
no_winner = True
while no_winner:
    for t in turtles:
        if t.xcor() > 230:
            winner = t.pencolor()
            no_winner = False
            break
        t.forward(random.randint(0, 5))

print(f"{winner.capitalize()} won the race!")
if winner == user_bet:
    print("You won!")
else:
    print("You lost")

screen.exitonclick()