from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)

# tim.color("red")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


########################################################### MANY SHAPES

# sides = 3
# total_angle = 180
# colors = ["royal blue", "aquamarine", "dark violet", "sandy brown", "yellow", "lime green", "indigo"]
# for i in range(7):
#     one_angle = (180 - (total_angle / sides))
#     tim.color(colors[i])
#     for j in range(sides):
#         tim.forward(100)
#         tim.right(one_angle)
#     sides += 1
#     total_angle += 180


########################################################### RANDOM WALK

# colors = ["royal blue", "aquamarine", "dark violet", "sandy brown", "yellow", "lime green", "indigo"]
# angles = [90, 270]
# tim.width(5)
# for i in range(50):
#     tim.color(random.choice(colors))
#     tim.forward(random.randint(40, 80))
#     tim.right(random.choice(angles))


########################################################### TURTLE CIRCLES

# tim.speed("fastest")

# def random_color():
#     r = random.randint(0, 255)
#     b = random.choice([0, 255])
#     g = 0
#     color_for_time = (r, g, b)
#     return color_for_time

# angle_change = 1
# iterations = int(360 / angle_change)
# for i in range(iterations):
#     tim.color(random_color())
#     len_1 = 100
#     tim.circle(len_1)
#     tim.right(angle_change)


########################################################### HIRST PAINTING

tim.speed("fastest")
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(10):
    for j in range(10):
        tim.color(random_color())
        tim.dot(10)
        tim.penup()
        tim.forward(20)
        tim.pendown()
    tim.color(random_color())
    tim.dot(10)

    val_1 = 270
    if(i % 2 == 0):
        val_1 = 90

    tim.right(val_1)
    tim.penup()
    tim.forward(20)
    tim.pendown()
    tim.right(val_1)


screen.exitonclick()