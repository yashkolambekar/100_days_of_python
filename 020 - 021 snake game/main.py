from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

move_snake = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while move_snake:
    time.sleep(0.1)
    screen.update()
    
    if snake.snake[0].distance(food) < 15:
        score.add_score()
        food.refresh()
        snake.add_tail()

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280:
        move_snake = False
    if snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        move_snake = False

    for seg in snake.snake:
        if seg == snake.snake[0]:
            pass
        elif snake.snake[0].distance(seg) < 10:
            move_snake = False

    snake.move()

screen.exitonclick()