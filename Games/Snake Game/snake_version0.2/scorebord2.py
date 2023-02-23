from turtle import Turtle

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {self.score}", align="center", font=("courier", 13,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("courier", 13, "normal"))

    def increse_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align="center", font=("courier", 13, "normal"))
