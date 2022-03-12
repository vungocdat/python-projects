# Famous game Pong

from screen import SetScreen
from paddle import Paddle
from ball import Ball
import turtle as t
import time


# set gaming screen
screen = t.Screen()
screen.tracer(0)  # turn off the animation
screen.bgcolor("black")
screen.title("Pong")
set_screen = SetScreen()

# set left and right paddles
paddle_left = Paddle(-350)
paddle_right = Paddle(350)


# allow paddles to move
screen.listen()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

# set a ball
ball = Ball()



game = True
while game:
    screen.update()
    time.sleep(0.05)
    ball.move()


screen.exitonclick()


