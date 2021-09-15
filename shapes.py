import turtle
from random import random
turtle.speed(100)
turtle.colormode(255)


def poly(sides, size):
    for x in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)


def thing(size):
    for x in range(12):
        turtle.pencolor((0 + x * 20), 0, (255 - x * 20))
        poly(x+3, size)


def something(sides, size):
    for x in range(sides):
        thing(size)
        turtle.forward(size)
        turtle.left(360/sides)


something(6, 25)

turtle.penup()
turtle.exitonclick()
