import turtle

turtle.speed(100)
turtle.colormode(255)
turtle.pensize(1)



def poly(sides, size):
    for x in range(sides):
        turtle.forward(size/2)
        turtle.right(360/sides)


def thing(size):
    for x in range(20):
        poly(x+2, size)
        turtle.pencolor((0 + x * 11 ), 0, (255 - x * 8))


def something(sides, size):
    for x in range(sides):
        thing(size)
        turtle.forward(size/2)
        turtle.left(360/sides)


something(5, 60)

turtle.penup()
turtle.exitonclick()
