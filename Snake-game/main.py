# Snake minigame

import turtle as t
import time
from snake import Snake
from food import Food

screen = t.Screen()
screen.title("Retro snake game")

snake = Snake()
food = Food()

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

    # detect the head of the snake is near the food (to be considered eaten) then show the food elsewhere
    if snake.head.distance(food) < 15:
        food.show_food()



screen.exitonclick()
