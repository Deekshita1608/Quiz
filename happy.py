
import turtle
import time
'''window=turtle.Screen()
window.bgcolor('black')'''
sethi=turtle.Turtle()
sethi.getscreen().bgcolor('black')

def go(a,b):
        sethi.goto(x=a,y=b)

def eyes(x):
        sethi.pendown()

        sethi.begin_fill()
        sethi.color("black")
        sethi.circle(x)
        sethi.end_fill()
        sethi.penup()

def whitedot(x):
    sethi.pendown()
    sethi.begin_fill()
    sethi.color("white")
    sethi.circle(x)
    sethi.end_fill()
    sethi.penup()


    
    
time.sleep(5)    
#face    
sethi.speed(1000)
sethi.color("yellow")
sethi.begin_fill()
sethi.penup()
go(0,-150)
sethi.pendown()
sethi.circle(150)
sethi.end_fill()
sethi.penup()
#left eye

go(-45,40)
eyes(16)
go(-45,35)
eyes(17)
go(-45,30)
eyes(19)
go(-45,25)
eyes(20)
go(-45,20)
eyes(21)
go(-45,15)
eyes(22)
go(-45,10)
eyes(22)
go(-45,5)
eyes(21)
go(-45,0)
eyes(20)
go(-45,-5)
eyes(18)
#ldot
go(-40,42)
whitedot(10)
go(-40,38)
whitedot(11)
go(-40,36)
whitedot(11)
go(-40,34)
whitedot(10)
#right eye
go(45,40)
eyes(16)
go(45,35)
eyes(17)
go(45,30)
eyes(19)
go(45,25)
eyes(20)
go(45,20)
eyes(21)
go(45,15)
eyes(22)
go(45,10)
eyes(22)
go(45,5)
eyes(21)
go(45,0)
eyes(20)
go(45,-5)
eyes(18)
#rdot
go(40,42)
whitedot(10)
go(40,38)
whitedot(11)
go(40,36)
whitedot(11)
go(40,34)
whitedot(10)

#smile
go(-75,-60)
sethi.color("black")
sethi.pendown()
sethi.speed(30)
sethi.pensize(10)
sethi.setheading(-45)
sethi.circle(100,95)
sethi.penup()
sethi.color("green")
go(0,-220)
sethi.write("Well Done!!...That\'s correct",align='center',font=('Cookie',25,'bold'))
time.sleep(5)



