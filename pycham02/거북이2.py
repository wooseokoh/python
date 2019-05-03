import turtle
import random

color = ['red','blue','green','yellow']
def leftclick(x,y):
    print('x축: ',x ,',','y축: ',y)
    width = 50
    height = 50

    c = random.randint(0,3)
    myTurtle.pencolor(color[c])
    sx1 = x - width
    sy1 = y - height
    myTurtle.goto(sx1, sy1)
    # myTurtle.penup() # 이동만!
    # myTurtle.goto(200, 200)
    # myTurtle.pendown() # 그림을 그리며 이동
    # myTurtle.goto(100, 100)

myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요')
myTurtle.pensize(20)
myTurtle.pencolor('blue')
# 클릭 했을떄 onscreenclick 메소드가 x,y축 값을 leftclick에 넣어서 호출
turtle.onscreenclick(leftclick, 1)
turtle.done()