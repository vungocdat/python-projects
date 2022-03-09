# Snake minigame

import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.title("Retro snake game")

snake = Snake()

# listen to take input from the user (on arrow keys)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.tracer(0)
snake_alive = True
while snake_alive:
    screen.update()  # update the screen -> shows the snake
    time.sleep(0.1)
    snake.move()



screen.exitonclick()
