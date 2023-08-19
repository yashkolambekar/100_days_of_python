from turtle import Turtle
import random

class Food(Turtle):
    
    def refresh(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x=x, y=y)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
