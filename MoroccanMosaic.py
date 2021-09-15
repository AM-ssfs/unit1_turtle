import turtle
turtle.speed(10)

def diamond(a, b):
    for x in range(2):
        turtle.forward(a)
        turtle.right(360/b)
        turtle.forward(a)
        turtle.right(180-360/b)


def diamond2(a, b):
    for x in range(b*2):
        diamond(a, b)
        turtle.right(180/b)

diamond2(30, 5)
turtle.exitonclick()
