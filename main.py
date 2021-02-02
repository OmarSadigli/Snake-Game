from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food.
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for part in snake.snake[1:]:
        if snake.snake[0].distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
