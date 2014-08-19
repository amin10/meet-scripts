import turtle

turtle.setup(width=1000,height=400)

#Cool customization
turtle.title('Thank You')
turtle.pensize(15)
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
    if x == None:
        x = turtle.xcor()
        y = turtle.xcor()
    go(x,y)
    turtle.goto(x+h/2 ,y)
    turtle.goto(x,y)
    turtle.goto(x,h/2+y)
    turtle.goto(x+h/2,h/2+y)
    turtle.goto(x,y+h/2)
    turtle.goto(x,y+h)
    turtle.goto(x+h/2,y+h)
    go(x+h,y)
def draw_backward_e(x,y,h=100):
    if x == None:
        x = turtle.xcor()
        y = turtle.xcor()
    go(x,y)
    turtle.goto(x+h/2 ,y)
    turtle.goto(x+h/2,h/2+y)
    turtle.goto(x,h/2+y)
    turtle.goto(x+h/2,y+h/2)
    turtle.goto(x+h/2,y+h)
    turtle.goto(x,y+h)
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
        turtle.left(1.14)
    turtle.left(180)
    for i in range(210):
        turtle.forward(1)
        turtle.right(1.14)
    go(x+h+20, y)
def draw_i(x,y,h=100):
    go(x+0.45*h,y)
    turtle.goto(x+0.9*h, y)
    turtle.goto(x,y)
    turtle.goto(x+0.45*h,y)
    turtle.goto(x+0.45*h,y+h)
    turtle.goto(x,y+h)
    turtle.goto(x+0.9*h,y+h)
    go(x+h+20,y)
def draw_z(x,y,h=100):
    #x,y is the point at the bottom left of the box which contains the letter
    width=int(2*h/3)
    go(x,y+h)
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
def heart(x,y,h=100):
    go(x,y)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.goto(x-h/2, y+0.75*h)
    turtle.seth(90)
    turtle.circle(-h/4, extent=180)
    turtle.seth(90)
    turtle.circle(-h/4, extent=180)
    turtle.goto(x,y)
    turtle.end_fill()
    go(x+h/2,y)

startx = -280
starty = -100
turtle.speed(3)
turtle.color("orange")
draw_m(startx-150,starty, 250)
draw_i(startx+125,starty)
turtle.color("white")
draw_e(startx+125, starty+150)
turtle.speed(0)
draw_c(startx+240,starty)
turtle.speed(3)
turtle.color("orange")
draw_backward_e(startx+220, starty+150)
draw_h(startx+355,starty)
draw_e(startx+455,starty)
draw_l(startx+560,starty)
draw_backward_e(startx+650,starty)
turtle.color("white")
draw_t(startx+300,starty+150)
turtle.color("orange")
heart(startx+500,starty+150)

turtle.ht()

turtle.mainloop()