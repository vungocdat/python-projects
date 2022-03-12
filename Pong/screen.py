# set game screen with size of height = 600 and width = 800

import turtle as t

t.colormode(1)

MAX_X = 400
MAX_Y = 300


class SetScreen(t.Turtle):

    # Set screen to black and draw the edges of the game
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(MAX_X, MAX_Y)
        self.pendown()
        self.pencolor("white")
        self.width(10)
        self.goto(-MAX_X, MAX_Y)
        self.goto(-MAX_X, -MAX_Y)
        self.goto(MAX_X, -MAX_Y)
        self.goto(MAX_X, MAX_Y)
        # draw a middle line
        self.goto(0, MAX_Y)
        self.setheading(270)
        self.penup()
        self.forward(8)  # adjust to make middle line look better
        self.pensize(3)
        while self.ycor() > -MAX_Y:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    @staticmethod
    def get_max_x():
        return MAX_X

    @staticmethod
    def get_max_y():
        return MAX_Y
