import turtle
import random

color = ['red','blue','green','yellow']

def leftclick(x,y):
    print('x축: ',x ,',','y축: ',y)

    n = random.randrange(1, 20)
    myTurtle.pensize(n)

    # 없어도 됨
    width = random.randint(20,200)
    height = random.randint(20,200)

    c = random.randint(0,3)
    myTurtle.pencolor(color[c])

    sx1 = x - width/2
    sy1 = y - height/2

    sx2 = x + width/2
    sy2 = y + height/2

    myTurtle.penup()
    myTurtle.goto(sx1, sy1)

    myTurtle.pendown()
    myTurtle.goto(sx1, sy2)
    myTurtle.goto(sx2, sy2)
    myTurtle.goto(sx2, sy1)
    myTurtle.goto(sx1, sy1)


myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요')
turtle.onscreenclick(leftclick, 1)
turtle.done()