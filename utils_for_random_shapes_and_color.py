from random import randint
def draw_polygon(t,sides,length):
    angle=360/sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

def move(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def get_random_colors():
    colors =['violet','indigo','blue','green','yellow','orange','red']
    return colors[randint(0,len(colors)-1)]
# def circle(t,radius):
#     t.circle(radius)