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
    screen.update() # update the screen -> shows the snake
    time.sleep(0.1)
    for i in snake:
        i.forward(10)

# next step is to made snake moving in a way that last part will go to the previous part etc
# udemy 185 - 12:00



screen.exitonclick()
