from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
    
    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            s = Turtle()
            s.penup()
            s.shape("square")
            s.width(20)
            s.color("white")
            s.setpos(x=x, y=y)
            self.snake.append(s)
            x -= 20

    def move(self):
        for s_no in range(len(self.snake) - 1,0,-1):
            new_x = self.snake[s_no - 1].xcor()
            new_y = self.snake[s_no - 1].ycor()
            self.snake[s_no].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
    
    def add_tail(self):
        x = self.snake[len(self.snake) - 1].xcor()
        y = self.snake[len(self.snake) - 1].ycor()
        s = Turtle()
        s.penup()
        s.shape("square")
        s.width(20)
        s.color("white")
        s.setpos(x=x, y=y)
        self.snake.append(s)

    def up(self):
            if not (self.snake[0].heading() == 270):
                self.snake[0].setheading(90)

    def down(self):
        if not (self.snake[0].heading() == 90):
            self.snake[0].setheading(270)
        
    def right(self):
        if not (self.snake[0].heading() == 180):
            self.snake[0].setheading(0)

    def left(self):
        if not (self.snake[0].heading() == 0):
            self.snake[0].setheading(180)