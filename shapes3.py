import turtle

turtle.speed(10)
turtle.pensize(2)
turtle.bgcolor("black")


def poly(sides2, size, color):
    for x in range(sides2):
        turtle.color(color)
        turtle.forward(size)
        turtle.left(360/sides2)
    turtle.forward(size)


def something(sides, size, sides2):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color = -1
    for x in range(sides):
        if color >= 6:
            color = -1
        color = color + 1
        poly(sides2, size, colors[color])
        turtle.right(360/sides)



def thing(sides, size):
    sides2 = 2
    for x in range(10):
        sides2 = sides2+1
        something(sides, size, sides2)


thing(6, 30)


turtle.exitonclick()
