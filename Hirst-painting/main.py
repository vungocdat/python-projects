# the program will create a similar painting as mr Hirst's spot painting
# program will print dots 10x10 with size of 20 and distance of 50

# After running this program save the list to save time from running it again
# import colorgram
#
# # Extract 10 colors from an image
# num_of_colors = 30
# colors = colorgram.extract('hirst_spot_painting.jpg', num_of_colors)
# print(colors)
#
# # creating list of tuples after extracting the colors
# color_list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_list.append((r, g, b))

import turtle as t
import random


def line_of_dots():
    for i in range(10):
        arrow.dot(20, random.choice(colors))
        arrow.fd(50)


t.colormode(255)
colors = [(249, 248, 248), (237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
          (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31),
          (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145),
          (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216),
          (100, 218, 229), (117, 171, 192), (79, 135, 178)]

arrow = t.Turtle()
screen = t.Screen()
arrow.penup()
position_y = 200

for i in range(10):
    arrow.setx(-200)
    arrow.sety(position_y)
    line_of_dots()
    position_y -= 50

arrow.hideturtle()

screen.exitonclick()

