# Famous game Pong

from screen import SetScreen
from paddle import Paddle
import turtle as t

# set gaming screen
screen = t.Screen()
screen.tracer(0)  # turn off the animation
screen.bgcolor("black")
screen.title("Pong")
set_screen = SetScreen()

# set left and right paddles
paddle_left = Paddle()
paddle_left.set_left()
paddle_right = Paddle()
paddle_right.set_right()

# allow paddle to move
screen.listen()
screen.onkey(paddle_left.move_up, "Up")
screen.onkey(paddle_left.move_down, "Down")



game = True
while game:
    screen.update()


screen.exitonclick()


