from turtle import Turtle


class Paddle:
    def __init__(self):
        self.bar = []
        self.creat_paddle()
        self.bar[0].goto(-380, 0)
        self.bar[1].goto(375, 0)

    def creat_paddle(self):
        for i in range(2):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.color("white")
            self.bar.append(paddle)

    def goup1(self):
        # self.bar.forward(10)
        y = self.bar[0].ycor()
        self.bar[0].goto(self.bar[0].xcor(), y+10)

    def goup2(self):
        # self.bar.forward(10)
        y = self.bar[1].ycor()
        self.bar[1].goto(self.bar[1].xcor(), y + 10)

    def godown1(self):
        # self.bar.forward(-10)
        y = self.bar[0].ycor()
        self.bar[0].goto(self.bar[0].xcor(), y - 10)

    def godown2(self):
        # self.bar.forward(-10)
        y = self.bar[1].ycor()
        self.bar[1].goto(self.bar[1].xcor(), y - 10)
