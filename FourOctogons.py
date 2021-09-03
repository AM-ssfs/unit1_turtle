Import turtle

x = 0
y = 0

While(x<4): 	  #makes 4 of the shapes

  While(y<8): 	#makes an octogon

    turtle.foward(25)     #side length 25 units
    turtle.right(22.5)    #rotates 180/8 deg
    y = y + 1             #when this happens 8 times the loop will break

  turtle.right(90)		#rotates turtle so ready for next shape
  turtle.foward(80)	  #turtle moves so octagons not overlap
  y = 0        #makes the octogon loop run again
  x = x + 1    #when this happens 4 times the loop will break
  
turtle.ExitOnClick()
