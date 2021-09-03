Import turtle

x = 0
y = 0

While(x<4):	#makes 4 of the shapes

  While(y<8):	#makes a 8 sided shape

    turtle.foward(25)
    turtle.right(22.5)
    y = y+1

  turtle.right(90)		#rotates turtle so ready for next shape
  turtle.foward(80)	#turtle moves so octagons not overlap
  y = 0
  x = x + 1
  
turtle.ExitOnClick()
