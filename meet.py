import turtle

#Cool customization
turtle.title('Thank You')
turtle.pensize(10)
turtle.shape('circle')
turtle.shapesize(2,2)
turtle.bgcolor('blue')

#Get to starting position
turtle.up()
turtle.goto(-300,0)
turtle.down()

#turtle.color('orange')
#M
turtle.goto(-300,100)
turtle.goto(-250, 50)
turtle.goto(-200, 100)
turtle.goto(-200, 0)
def go(x,y)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
def draw_e(x,y,h=100):
    #Get to E:


    #turtle.color('white')
    #E
    turtle.goto(x-h/2 ,y)
    turtle.goto(x-h/2,h/2+y)
    turtle.goto(x,h/2+y)
    turtle.goto(x-h/2,y+h/2)
    turtle.goto(x-h/2,y+h)
    turtle.goto(x,y+h)

def draw_l(x,y,h=100):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()







# #### Ted's stuff
def draw_z(x,y,h=100):
    #x,y is the point at the bottom left of the box which contains the letter
    width=int(2*h/3)
    turtle.go(x,y+h)
    turtle.pendown()
    turtle.goto(x+width,y+h) #Draw top line of Z
    turtle.goto(x,y) #Draw diagonal line of Z
    turtle.goto(x+width,y) #Draw bottom horizontal line of Z
    go(x+width+int(h/6),y) #Go to right side of box containing letter and add space

draw_e(-100,0)
draw_e(0,0)

#Get to T:
turtle.up()
turtle.goto(100,0)
turtle.down()

#turtle.color('white')
#T
turtle.goto(100,100)
turtle.goto(50,100)
turtle.goto(150,100)

turtle.ht() #Hide the Turtle!

turtle.mainloop()

#This is a test - Ted
