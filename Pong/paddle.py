import turtle as t
from screen import SetScreen

MAX_Y = SetScreen.get_max_y() - 60      # -60 to adjust to the length of the paddle


class Paddle(t.Turtle):

    # create a paddle
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(position_x)

    def move_up(self):
        if self.ycor() < MAX_Y:
            position_y = self.ycor() + 20
            self.sety(position_y)

    def move_down(self):
        if self.ycor() > -MAX_Y:
            position_y = self.ycor() - 20
            self.sety(position_y)
