import turtle
turtle.speed(100)
turtle.colormode(255)
turtle.pensize(1)



def poly(sides, size):
    for x in range(1, sides+1):
        turtle.pencolor((0 + x), 0, (255 - x))
        turtle.forward(size)
        turtle.right(360/sides*((x**1.05)/x))



poly(255,3)
turtle.exitonclick()
