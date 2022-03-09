import turtle as t

MAX_X = 400
MIN_X = -400
MAX_Y = 400
MIN_Y = -400


# Draw the borderlines
# static methods return max and min values
class SetScreen(t.Turtle):

    # draw the edges of the game
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(MAX_X, MAX_Y)
        self.pendown()
        self.setx(MIN_X)
        self.sety(MIN_Y)
        self.setx(MAX_X)
        self.sety(MAX_Y)

    @staticmethod
    def get_max_x():
        return MAX_X

    @staticmethod
    def get_max_y():
        return MAX_Y

    @staticmethod
    def get_min_x():
        return MIN_X

    @staticmethod
    def get_min_y():
        return MIN_Y
