import turtle as t
import time
from screen import SetScreen


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)  # start in the middle
        self.speed("slowest")
        self.x_move = 0.06
        self.y_move = 0.06

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # reverse the movement of the Y
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # ball start off the center again and with the opposite direction
    def reset_position(self):
        self.goto(0, 0)
        time.sleep(1)
        self.bounce_x()