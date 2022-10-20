
import turtle
tao = turtle.Pen()#Open the function Pen
tao.shape('turtle') #Change form to Turtle

def Rectangle():
    '''The Square'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Circle():
    '''The Circle'''
    for i in range(10):
        tao.circle(50)
        tao.left(36)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Go(200,200)
Rectangle()
Circle()
Go(-200,-200)
Rectangle()
Circle()
Go(0,0)
Circle()
