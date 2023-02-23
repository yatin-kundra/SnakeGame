import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import ScoreBord


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
l_scorebord = ScoreBord((-80,280),1)
r_scorebord = ScoreBord((80,280),2)
screen.update()
screen.tracer(1)
screen.update()
ball = Ball()


screen.listen()
screen.onkeypress(fun=paddle_r.go_up, key="Up")
screen.onkeypress(fun=paddle_r.go_down, key="Down")
screen.onkeypress(fun=paddle_l.go_up, key="w")
screen.onkeypress(fun=paddle_l.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    # screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bonce()
    # collition will paddle
    # ball.move_ball()
    # if ball.distance(paddle_l) < 50:
    #     ball.move_ball()
    # if ball.distance(paddle_r) < 50:
    #     ball.move_ball()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) <50 and ball.xcor() <-320:
        ball.bonce_x()

    if ball.xcor() >= 500:
        # l_scorebord.increse_score(1)
        screen.tracer(0)
        ball.reset_pos()
        screen.update()


    if ball.xcor() <= -500:
        # r_scorebord.increse_score(2)
        screen.tracer(0)
        ball.reset_pos()
        screen.update()
        screen.tracer(1)


screen.exitonclick()
