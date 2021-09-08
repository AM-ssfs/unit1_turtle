import turtle
from random import random

x = 0
y = 0

turtle.speed(9999)  #ZOOOOOOOOM! fast turtle :)

while(x<100):#makes 100 of the octogons bellow

  while(y<8):#makes an octogon

    turtle.forward(80)     #side length 80 units
    turtle.right(45)       #rotates
    y = y + 1              #when this happens 8 times the loop will exit

  turtle.right(3.6)	  #rotates turtle so ready for next shape
  y = 0        #makes the octogon loop run again
  x = x + 1    #when this happens enough times the loop will break
turtle.penup()  #stops drawing
turtle.exitonclick()  #so it doesn't automaticaly close when it runs
