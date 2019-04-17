from tkinter import *
from file import 메인모듈

w = None

def endCall2():
    global w2
    w2.destroy()
    메인모듈.recall()

def call():
    global w2
    w2 = Tk()
    
    b = Button(w2, text = "메인모듈로 가요.", command = endCall2)
    
    b.pack()
    
    w2.mainloop()
    
