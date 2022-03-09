import turtle as t


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.sety(400)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def add_point(self):
        self.score += 1
