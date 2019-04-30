from tkinter import *
from cloud.function import *
from tkinter import messagebox
from cloud.db import *

def closecallback():

    messagebox.showinfo("종료", "종료합니다")
    w.destroy()

w = Tk()

w.geometry("200x200")
w.title("수강관리프로그램")

insert = Button(w, text = "입력", command = insert_infor)
printall = Button(w, text = "출력", command = printall_infor)
update = Button(w, text = "수정", command = update_infor)
arrange = Button(w, text = "정리", command = arrange_result)
exit = Button(w, text = "종료", command=closecallback)

insert.pack()
printall.pack()
update.pack()
arrange.pack()
exit.pack()

w.mainloop()
