import turtle as t
import screen as s


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.sety(s.MAX_X)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 30, "normal"))

    def add_point(self):
        self.score += 1
