import turtle

x = 0
y = 0

while(x<4):#makes 4 of the octogons bellow

  turtle.fillcolor("red")
  turtle.begin_fill()

  while(y<8):#makes an octogon

    turtle.forward(25)     #side length 25 units
    turtle.right(45)    #rotates 180/8 deg
    y = y + 1             #when this happens 8 times the loop will break
  turtle.end_fill()
  turtle.right(90)	  #rotates turtle so ready for next shape
  turtle.penup()
  turtle.forward(80)	  #turtle moves so octagons not overlap
  turtle.pendown()
  y = 0        #makes the octogon loop run again
  x = x + 1    #when this happens 4 times the loop will break
  
turtle.exitonclick()  #so it doesn't automaticaly close when it runs
