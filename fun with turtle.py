import turtle

def star():
    turtle.left(10)
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    for x in range(5):
        turtle.forward(50)
        turtle.left(20)
        turtle.back(50)
        turtle.right(460/5)
    turtle.end_fill()
    turtle.left(460/5)

def pentagon():
    turtle.forward(50)
    turtle.right(65)
    turtle.pensize(5)
    for x in range(5):
        turtle.right(360/5)
        turtle.forward(72)


star()
pentagon()
turtle.exitonclick()
