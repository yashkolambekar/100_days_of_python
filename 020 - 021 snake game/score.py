from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setpos(x=0, y=270)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.value}", font=("Arial", 16, "normal"), align="center")

    def add_score(self):
        self.value += 1
        self.update_score()
