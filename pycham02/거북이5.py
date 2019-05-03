import turtle
import random

class Shape:

    sx, sy = [0] * 2
    myTurtle = None

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')

    def set(self):
        r = random.random()
        g = random.random()
        b = random.random()

        n = random.randrange(1, 20)
        self.myTurtle.pensize(n)
        self.myTurtle.pencolor((r,g,b))

    def drawShape(self):
        pass

class Star(Shape):

    def __init__(self,x,y):

        self.sx = x
        self.sy = y
        Shape.__init__(self)

    def drawShape(self):
        self.myTurtle.penup()
        self.myTurtle.goto(self.sx,self.sy)

        self.set()
        self.myTurtle.pendown()
        while True:
            self.myTurtle.left(127)
            self.myTurtle.forward(100)

def leftclick(x,y):

    data = int(input("네모는 1번 별은 2번 :"))

    if data == 1:
        pass
    if data == 2:
        star = Star(x,y)
        star.drawShape()


turtle.title('거북이로 그림을 그려요')
turtle.onscreenclick(leftclick, 1)
turtle.done()