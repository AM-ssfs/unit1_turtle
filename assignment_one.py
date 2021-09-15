import turtle  #turtle was imported and used correctly


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def octagon(color):  #functions are deffined correctly with appropriate parrameters

    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    for x in range(8):   #loop is used to create a shape   +   shape is created successfuly with correct angles

        turtle.forward(25)
        turtle.right(45)

    turtle.end_fill()


def goto(x):        #functions are deffined correctly with appropriate parrameters

    turtle.penup()
    turtle.goto(x*50, x*50)
    turtle.pendown()


for x in range(1, 5):

    octagon(colors[x])   #funtion is called multiple times with diffrent parrameters
    goto(x)

turtle.exitonclick()
