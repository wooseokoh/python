from tkinter import *
from tkinter.ttk import *
import random
import time
import threading

class ProgressThread:
    thread = None
    progress = None

    #생성자 - 프로그래스바 생성
    def __init__(self, parent):
        self.progress = Progressbar(parent, orient = HORIZONTAL, length = 500)
        self.progress.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)
        self.thread = threading.Thread(target=self.progressRun, args=(self.progress, ))
        self.thread.start()

    #함수 - 경기내용 구현해주는 부분
    def progressRun(self,progress):
        jump = 0
        while True:
            jump = random.randrange(0,10)
            if progress['value'] >= 100:
                break
            progress['value'] = progress['value'] + jump
            time.sleep(0.5)

def runProgress():
    bar1 = ProgressThread(w)
    bar2 = ProgressThread(w)
    bar3 = ProgressThread(w)


if __name__ == '__main__':
    w = Tk()
    w.geometry("300x250")
    w.title("멀티 스레드 프로그래스 바")
    b = Button(w, text='멀티 스레드 시작', command = runProgress)
    b.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)

    w.mainloop()