import random
import turtle
from turtle import Turtle
turtle.colormode(255)
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_box = []
        self.creat_snake()
        self.head = self.snake_box[0]
        self.head.color(self.random_color())
        self.head.shape("triangle")
        self.head.shapesize(1.3)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        randmoncolor = (r, g, b)
        return randmoncolor

    def creat_snake(self):      # this function will creat snake and give it it's attributes
        for turtle in range(3):
            # self.add_segment(len(self.snake_box))
            sq = Turtle(shape="square")
            sq.penup()
            sq.color(self.random_color())
            sq.speed("fastest")
            self.snake_box.append(sq)

            j = 0
            for i in self.snake_box:
                self.snake_box[j].goto(x=j * 20, y=0)
                j += 1


    # def add_segment(self, no_of_boxes):
    #     sq = Turtle(shape="square")
    #     sq.penup()
    #     sq.color("white")
    #     sq.speed("fastest")
    #     self.snake_box.append(sq)
    #
    #     j = 0
    #     for i in self.snake_box:
    #         self.snake_box[j].goto(x=j * 20, y=0)
    #         j += 1
    #
    # def extend_snake(self):
    #     self.add_segment(self.snake_box[-1].position())

    def extend_sanke(self):
        sq = Turtle(shape="square")
        sq.penup()
        sq.color(self.random_color())
        sq.speed("fastest")
        self.snake_box.append(sq)
        x = self.snake_box[-2].xcor()
        y = self.snake_box[-2].ycor()
        self.snake_box[-1].goto(x,y)

    def move(self):
        for seg in range(len(self.snake_box) - 1, 0, -1):
            new_x = self.snake_box[seg - 1].xcor()  # 3rd box goes to 2nd , 2nd goes to 1st , and 1st moves forward
            new_y = self.snake_box[seg - 1].ycor()
            self.snake_box[seg].goto(new_x, new_y)
        self.snake_box[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


