# Snake minigame

import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.title("Retro snake game")

snake = Snake()

screen.tracer(0)
snake_alive = True
while snake_alive:
    screen.update()  # update the screen -> shows the snake
    time.sleep(0.1)



screen.exitonclick()
