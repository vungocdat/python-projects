import turtle as t

STARTING_BODY = 3  # number of squares
VELOCITY = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # constructor which will create a snake with 3 parts from 'create_snake' method
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # snake comes out from a hole
    def create_snake(self):
        for i in range(STARTING_BODY):
            i = (0, 0)
            self.add_body(i)

    def add_body(self, position):
        snake_body = t.Turtle(shape="square")
        snake_body.penup()  # to not draw a line while moving
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend_body(self):
        self.add_body(self.snake[-1].position())

    def move(self):
        # start moving the last part of snake and move it to the position, where the previous part was
        for i in range(len(self.snake) - 1, 0, -1):
            previous_x = self.snake[i - 1].xcor()
            previous_y = self.snake[i - 1].ycor()
            self.snake[i].goto(previous_x, previous_y)
        self.head.forward(VELOCITY)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
