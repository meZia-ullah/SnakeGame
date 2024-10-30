import time
import turtle
from turtle import Turtle, Screen
from food import Food
from MoveSnake import Move
from scorebroad import ScoreBroad

my_screen = Screen()
turtle.setup(600, 600)
turtle.tracer(0)
my_screen.bgcolor("black")

snake = Move()
food = Food()
score = ScoreBroad()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    snake.move()
    my_screen.update()
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            is_game_on = False
            score.game_over()

my_screen.exitonclick()
