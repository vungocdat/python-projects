import turtle as t

STARTING_BODY = 3


class Snake:

    # constructor which will create a snake with 3 parts from 'create_snake' method
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(STARTING_BODY):
            snake_body = t.Turtle(shape="square")
            snake_body.penup()  # to not draw a line while moving
            snake_body.setx(i * -20)
            self.snake.append(snake_body)

    def move(self):
        # start moving the last part of snake and move it to the position, where the previous part was
        for i in range(len(self.snake) - 1, 0, -1):
            previous_x = self.snake[i - 1].xcor()
            previous_y = self.snake[i - 1].ycor()
            self.snake[i].goto(previous_x, previous_y)
        self.snake[0].forward(20)
