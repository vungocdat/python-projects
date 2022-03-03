# Etch a sketch - draw by moving a turtle using 'w' 'a' 's' 'd' keys. Reset with 'c'

import turtle as t

turtle_1 = t.Turtle("turtle")
screen = t.Screen()


def move_forward():
    turtle_1.forward(10)


def move_backward():
    turtle_1.backward(10)


def turn_left():
    turtle_1.left(15)


def turn_right():
    turtle_1.right(15)


def reset_screen():
    screen.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")  # when passing a function as argument -> no (), using keywords recommended
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=reset_screen, key="c")
screen.exitonclick()
