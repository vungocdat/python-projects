# Famous game Pong

from screen import SetScreen
from paddle import Paddle
from ball import Ball
import turtle as t
from scoreboard import Scoreboard


# set gaming screen
screen = t.Screen()
screen.tracer(0)  # turn off the animation
screen.bgcolor("black")
screen.title("Pong")
set_screen = SetScreen()

# set left and right paddles
paddle_left = Paddle(-350)
paddle_right = Paddle(350)

# show scoreboard
scoreboard = Scoreboard()

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
    ball.move()

    # bouncing, number 20 because the size of the ball is 20 so it will bounce right when it hits the wall
    if ball.ycor() > (set_screen.get_max_y() - 20) or ball.ycor() < (-set_screen.get_max_y() + 20):
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # ball hits right end, left player gets a point
    if ball.xcor() > set_screen.get_max_x():
        scoreboard.add_point_to_left()
        ball.reset_position()

    if ball.xcor() < -set_screen.get_max_x():
        scoreboard.add_point_to_right()
        ball.reset_position()


screen.exitonclick()


