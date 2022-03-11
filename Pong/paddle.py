import turtle as t
from screen import SetScreen

LEFT_PADDLE = (350, 0)
RIGHT_PADDLE = (-350, 0)

MAX_Y = SetScreen.get_max_y() - 60      # -60 to adjust to the length of the paddlep


class Paddle(t.Turtle):

    # create a paddle
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def set_left(self):
        self.goto(LEFT_PADDLE)

    def set_right(self):
        self.goto(RIGHT_PADDLE)

    def move_up(self):
        if self.ycor() < MAX_Y:
            position_y = self.ycor() + 20
            self.sety(position_y)

    def move_down(self):
        if self.ycor() > -MAX_Y:
            position_y = self.ycor() - 20
            self.sety(position_y)
