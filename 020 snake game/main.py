from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

move_snake = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while move_snake:
    time.sleep(0.2)
    screen.update()

    snake.move()

screen.exitonclick()