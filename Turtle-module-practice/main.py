import turtle
import random


def draw_square(turtle_object_name):
    for i in range(4):
        turtle_object_name.rt(90)
        turtle_object_name.fd(100)


def draw_dash_line(turtle_object_name):
    turtle_object_name.fd(10)
    turtle_object_name.pu()
    turtle_object_name.fd(10)
    turtle_object_name.pd()


def draw_shape(turtle_name, sides_num):
    angle = 360 / sides_num
    turtle_name.pencolor(random_colour())
    for i in range(sides_num):
        turtle_name.rt(angle)
        turtle_name.fd(100)


def random_walk(turtle_ob, how_many_steps):
    turtle_ob.pensize(10)
    turtle_ob.speed(0)
    for i in range(how_many_steps):
        turtle_ob.pencolor(random_colour())
        turtle_ob.setheading(random.choice(direction))
        turtle_ob.fd(20)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    result = (r, g, b)
    return result


def draw_circles(obj_name, circle_num):
    angle = 360 / circle_num
    obj_name.speed(0)
    starting_circle = 0
    for i in range(circle_num):
        obj_name.pencolor(random_colour())
        obj_name.setheading(starting_circle)    # turns a turtle by a little
        obj_name.circle(100)
        starting_circle += angle


direction = [0, 90, 180, 270]

# to be able to change colour based on RBG colors
turtle.colormode(255)

tim = turtle.Turtle()
tim.shape("turtle")

# max_sides = 5
# for i in range(3, max_sides + 1):
#     draw_shape(tim, i)

# steps = 200
# random_walk(tim, steps)

# circles = 100
# draw_circles(tim, circles)

screen = turtle.Screen()
screen.exitonclick()
