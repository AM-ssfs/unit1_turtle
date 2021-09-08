import turtle

turtle.speed(25)

for x in range(5, 25):
    turtle.forward(x*2)
    turtle.right(90)

turtle.exitonclick()