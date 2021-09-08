import turtle

turtle.speed(100)
turtle.colormode(255)
turtle.pensize(1)


def poly(sides, size):
    for x in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)


def thing(size):
    for x in range(15):
        poly(x+2, size)


def something(sides, size):
    for x in range(sides):
        thing(size)
        turtle.forward(size)
        turtle.right(360/sides)


something(6, 25)

turtle.penup()
turtle.exitonclick()
