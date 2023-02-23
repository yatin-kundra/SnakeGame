import random
import time
from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.turn = [1, 0]
        # self.move_ball()
        # self.forward(100)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    #
    def move_ball(self):
        # ball will go to right
        if self.turn[0] == 1:
            angle = random.randint(-85, 280)
            self.setheading(angle)
            while self.colliosion():
                self.forward(20)
            self.bunce()
            self.turn[0] = 0
            self.turn[1] = 1
            return
        # ball will go to left
        if self.turn[1] == 1:
            angle = random.randint(-85+180, 280+180)
            self.setheading(angle)
            while self.colliosion():
                self.forward(10)
            self.bunce()
            self.turn[0] = 1
            self.turn[1] = 0
            return

    #
    def bunce(self):
        if self.ycor() > 280 and self.xcor() < 400:
            x = self.xcor() + 10
            y = self.ycor() - 10
            self.goto(x,y)

        elif self.ycor() > 280 and self.xcor() > -400:
            x = self.xcor() - 10
            y = self.ycor() - 10
            self.goto(x,y)

        elif self.ycor() < -280 and self.xcor() < 400:
            x = self.xcor() + 10
            y = self.ycor() + 10
            self.goto(x,y)

        elif self.ycor() < -280 and self.xcor() > -400:
            x = self.xcor() + 10
            y = self.ycor() + 10
            self.goto(x,y)
    #
    def colliosion(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return False
        else:
            return True

    def bonce(self):
        self.y_move *= -1

    def bonce_x(self):
        self.x_move *= -1

    def bonce_y(self):
        self.y_move *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.bonce_x()
