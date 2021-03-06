# Snake minigame

import turtle as t
import time
from snake import Snake
from food import Food
from scoreborard import Scoreboard
from screen import SetScreen

screen = t.Screen()
screen.title("Retro snake game")

set_screen = SetScreen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        snake.extend_body()
        scoreboard.add_point()
        scoreboard.display_score()

    # detect collision with the wall
    max_x = set_screen.get_max_x()
    max_y = set_screen.get_max_y()
    min_x = set_screen.get_min_x()
    min_y = set_screen.get_min_y()
    if snake.head.xcor() > max_x or snake.head.ycor() > max_y or snake.head.xcor() < min_x or snake.head.ycor() < min_y:
        snake_alive = False
        scoreboard.game_over()

    # detect collision with the body
    for i in snake.snake[1:]:   # loop through the list excluding the head (on position 0)
        if snake.head.distance(i) < 10:
            snake_alive = False
            scoreboard.game_over()

screen.exitonclick()
