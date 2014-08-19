import turtle

#Cool customization
turtle.title('Thank You')
turtle.pensize(10)
turtle.shape('circle')
turtle.shapesize(2,2)
turtle.bgcolor('blue')


def go(x,y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def draw_m(x,y,h=100):
    go(x,y)
    turtle.goto(x,y+h)
    turtle.goto(x+h/2, y+h/2)
    turtle.goto(x+h,y+h)
    turtle.goto(x+h, y)
    go(x+h+20,y)


def draw_e(x,y,h=100):
    go(x,y)
    turtle.goto(x+h/2 ,y)
    turtle.goto(x,y)
    turtle.goto(x,h/2+y)
    turtle.goto(x+h/2,h/2+y)
    turtle.goto(x,y+h/2)
    turtle.goto(x,y+h)
    turtle.goto(x+h/2,y+h)
    go(x+h,y)

def draw_l(x,y,h=100):
    go(x,y)
    turtle.goto(x, y+h)
    turtle.goto(x,y)
    turtle.goto(x+h/2, y)
    go(x+h,y)

def draw_h(x,y,h=100):
    go(x,y)
    turtle.goto(x,y+h)
    turtle.goto(x,y+h/2)
    turtle.goto(x+h/2, y+h/2)
    turtle.goto(x+h/2, y+h)
    turtle.goto(x+h/2, y)
    go(x+h,y)

def draw_c(x,y,h=100):
    go(x+h/2,y)
    for i in range(30):
        turtle.forward(1)
        turtle.left(1)
    turtle.left(180)
    for i in range(240):
        turtle.forward(1)
        turtle.right(1)








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

def draw_t(x,y,h=100):
    go(x+h/2, y)
    turtle.goto(x+h/2, y+h)
    turtle.goto(x,y+h)
    turtle.goto(x+h, y+h)
    go(x+h+20, y)



turtle.ht() #Hide the Turtle!

turtle.mainloop()

#This is a test - Ted
