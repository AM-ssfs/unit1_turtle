import turtle

turtle.speed(10)

def square(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


def house(size, color1, color2, number):
    for x in range(number):
        square(size, color1)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        triangle(size, color2)
        turtle.penup()
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size*2)
        turtle.pendown()


house(20, "blue", "red", 2)
house(40, "green", "black", 4)
house(15, "purple", "orange", 3)
turtle.exitonclick()