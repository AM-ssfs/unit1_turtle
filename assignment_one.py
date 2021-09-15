import turtle


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def octagon(color):

    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    for x in range(8):

        turtle.forward(25)
        turtle.right(45)

    turtle.end_fill()


for x in range(1, 5):

    octagon(colors[x])
    turtle.penup()
    turtle.goto(x*50, (x*50))
    turtle.pendown()

turtle.exitonclick()