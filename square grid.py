import turtle

turtle.speed(40)

for x in range(5):
    for x in range(5):
        for x in range(4):
            turtle.forward(10)
            turtle.right(90)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.penup()
    turtle.forward(-50)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()

turtle.exitonclick()