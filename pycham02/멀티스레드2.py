from tkinter import *
from tkinter.ttk import *
import random
import time
import threading

class ProgressThread:
    thread = None
    progress = None
    label = None
    xpick = 0
    ypick = 0
    #생성자 - 프로그래스바 생성
    def __init__(self, parent,label,x1,y1):

        self.label = Label(parent, text = "자동차")
        self.label.place(x = self.xpick, y = self.ypick)
        self.thread = threading.Thread(target=self.progressRun, args=(self.label,x1,y1, ))
        self.thread.start()

    #함수 - 경기내용 구현해주는 부분
    def progressRun(self, label, x1, y1):
        jump = 0
        while True:
            jump = random.randrange(0,10)
            if x1 >= 300:
                break
            x1 = x1 + jump
            label.place(x = x1, y = y1)
            time.sleep(0.1)

def runProgress():
    car1 = ProgressThread(w,"car1", 10, 100)
    car2 = ProgressThread(w,"car2", 10, 150)
    car3 = ProgressThread(w,"car3", 10, 200)


if __name__ == '__main__':
    w = Tk()
    w.geometry("300x250")
    w.title("멀티 스레드 프로그래스 바")
    b = Button(w, text='멀티 스레드 시작', command = runProgress)
    b.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)

    w.mainloop()