from turtle import  Screen
from bar import Paddle


screen = Screen()
paddle = Paddle()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")

screen.listen()
screen.onkeypress(fun=paddle.bar[0].goup1,key="Up")
screen.onkeypress(fun=paddle.bar[0].godown1,key="Down")
screen.onkeypress(fun=paddle.bar[1].goup2,key="w")
screen.onkeypress(fun=paddle.bar[1].godown2,key="s")

# paddle.goto(x=-390, y=0)

screen.update()

screen.exitonclick()
