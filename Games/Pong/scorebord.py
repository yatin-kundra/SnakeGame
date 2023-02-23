from turtle import Turtle

class ScoreBord(Turtle):
    def __init__(self,position,player):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"Player{player}: {self.score}", align= "center", font= ("courier",13,"normal"))


    def increse_score(self,player):
        self.clear()
        self.score += 1
        self.write(f"Player{player}: {self.score}", align= "center", font= ("courier",13,"normal"))
