import turtle

def leftclick(x,y):
    print('x축: ',x ,',','y축: ',y)

    myTurtle.penup() # 이동만!
    myTurtle.goto(200, 200)
    myTurtle.pendown() # 그림을 그리며 이동
    myTurtle.goto(100, 100)

myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요')
myTurtle.pensize(20)
myTurtle.pencolor('blue')
# 클릭 했을떄 onscreenclick 메소드가 x,y축 값을 leftclick에 넣어서 호출
turtle.onscreenclick(leftclick, 1)
turtle.done()