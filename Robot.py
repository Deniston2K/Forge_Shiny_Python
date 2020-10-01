import turtle
import PT_Utils_Robot
t=turtle.Turtle()
t.speed(5)
move=PT_Utils_Robot.move(t,0,150)
head=PT_Utils_Robot.head(t,50)
body=PT_Utils_Robot.body(t,150,90)
leg=PT_Utils_Robot.leg(t,100,30)
hand=PT_Utils_Robot.hand(t,100,60)
turtle.done()