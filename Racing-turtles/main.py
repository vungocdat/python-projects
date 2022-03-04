# Create 7 turtles and move them forward randomly
# the first one to reach the other end is the winner

import turtle as t
import random as r
from art import win, lose


def set_race():
    position_y = 300
    length = len(colors)
    for i in range(0, length):
        racing_turtle = t.Turtle(shape="turtle")
        racing_turtle.hideturtle()
        racing_turtle.shapesize(2)
        racing_turtle.penup()
        racing_turtle.color(colors[i])
        racing_turtle.goto(x=400, y=position_y)
        position_y -= 100
        racing_turtle.pendown()
        racing_turtle.setx(-400)
        racing_turtle.showturtle()
        racers.append(racing_turtle)    # add racing turtle to the list


def print_result(user_bet, turtle_winner):
    print(f"Your bet: {user_bet}\n")
    if user_bet == turtle_winner:
        print(win)
    else:
        print(lose)
        print(f"The winner is {turtle_winner} turtle.")



screen = t.Screen()
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
racers = []
set_race()


# show a pop-up window
bet = screen.textinput(title="Turtle race", prompt="What turtle is gonna win? Type a turtle's color: ").lower()

start_racing = False
if bet:
    start_racing = True

# move turtles randomly
while start_racing:
    for i in racers:
        if i.xcor() > 400:
            winner = i.pencolor()
            start_racing = False
            print_result(bet, winner)
        move = r.randint(0, 10)
        i.forward(move)

screen.exitonclick()
