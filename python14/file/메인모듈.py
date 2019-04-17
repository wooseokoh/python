from tkinter import *
from file import 호출모듈

w = None

def endCall():
    global w
    w.destroy()
    호출모듈.call()

def recall():
    global w
    w = Tk()
    
    b = Button(w, text = "호출모듈로 가요.", command = endCall)
    
    b.pack()
    
    w.mainloop()
    
if __name__ == '__main__':
    recall()