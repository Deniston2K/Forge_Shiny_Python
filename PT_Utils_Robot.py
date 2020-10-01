
def move(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def head(t,radius):
    t.circle(radius)
def body(t,length,angle):
    t.right(angle)
    t.forward(length)
def turn_back_start(t,length):
    t.left(180)
    t.forward(length)
def leg(t,length,L_angle):
    t.left(L_angle)
    t.forward(length)
    turn_back_start(t,length)
    t.left(180-2*L_angle)
    t.forward(length)
    turn_back_start(t,length)
def hand(t,length,H_angle):
    t.left(30)
    t.forward(75)
    leg(t,length,H_angle)




