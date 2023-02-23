import time
from snake import Snake
from food import Food
from scorebord import ScoreBord
from turtle import Screen

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)        #just turning off the transiton

snake = Snake()
food = Food()
scorebord = ScoreBord()

screen.listen()
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down")
screen.onkey(fun= snake.left, key="Left")
screen.onkey(fun= snake.right, key="Right")




game_on = True
while game_on:
    screen.update()     # cause we turned off the transition
    time.sleep(0.08)    # refresh rate for the update or pace of the snake
    snake.move()

    # detecting collision with the food
    if snake.head.distance(food) < 15 :
        scorebord.increse_score()
        snake.extend_sanke()
        food.random_movement()


    # detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scorebord.game_over()

    # ---- detecting collision with tail ----

    # for segment in snake.snake_box:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_on = False
    #         scorebord.game_over()

    # for i in range(0,len(snake.snake_box)):
    #     if snake.head == snake.snake_box[i]:
    #         pass
    #     elif snake.head.distance(snake.snake_box[i]) < 10:
    #         game_on = False
    #         scorebord.game_over()
















screen.exitonclick()