import turtle as t
import random as r
import screen as s


# inherits Turtle class from module turtle
class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")    # set the food in form of circle
        self.penup()    # do not draw a line where a new food appears
        self.color("red")
        self.speed("fastest")
        random_x = r.randint(-300, 300)
        random_y = r.randint(-300, 300)
        self.goto(random_x, random_y)
        self.show_food()

    # show food at random locations
    def show_food(self):
        random_x = r.randint(s.MIN_X, s.MAX_X)
        random_y = r.randint(s.MIN_Y, s.MAX_Y)
        self.goto(random_x, random_y)

