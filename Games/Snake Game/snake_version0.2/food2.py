from turtle import Turtle,Screen
import random, time



# sceen = Screen()
# sceen.bgcolor("black")
# sceen.tracer(0)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5)
        self.random_movement()

    def random_movement(self):
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        self.goto(x, y)

# food = Food()
# for i in range(7):
#     sceen.update()
#     food.random_movement()
#     time.sleep(1)
#
#
#
# sceen.exitonclick()