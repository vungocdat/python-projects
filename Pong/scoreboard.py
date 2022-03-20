import turtle as t


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.goto(-100, 175)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 175)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    # methods will update scoreboard by adding one point to the winner
    def add_point_to_left(self):
        self.left_score += 1
        self.show_scoreboard()

    def add_point_to_right(self):
        self.right_score += 1
        self.show_scoreboard()
