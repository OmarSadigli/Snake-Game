from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snake.append(new_snake)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
