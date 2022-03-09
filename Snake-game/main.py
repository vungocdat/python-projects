# Snake minigame

import turtle as t
import time

screen = t.Screen()
screen.title("Retro snake game")

snake = []

# Create starting snake with size of 3 squares
starting_body = 3
for i in range(starting_body):
    snake_body = t.Turtle(shape="square")
    snake_body.penup()  # to not draw a line while moving
    snake_body.setx(i * -20)
    snake.append(snake_body)

screen.tracer(0)
snake_alive = True
while snake_alive:
    screen.update()  # update the screen -> shows the snake
    time.sleep(0.1)
    # start moving the last part of snake and move it to the position, where the previous part was
    for i in range(len(snake) - 1, 0, -1):
        previous_x = snake[i - 1].xcor()
        previous_y = snake[i - 1].ycor()
        snake[i].goto(previous_x, previous_y)

    snake[0].forward(20)
    snake[0].left(90)



screen.exitonclick()
