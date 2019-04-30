from cloud.db import *
from tkinter import *

# 전역변수설정
id_input,classes_input,content_input,cost_input,member_input = None,None,None,None,None
w,w1 = None,None
data = None

def insert_infor():
    
    global id_input,classes_input,content_input,cost_input,member_input
    global w
    w1 = Tk()

    w1.geometry("300x300")
    w1.title("등록")
    
    id = Label(w1, text = "수강아이디")
    classes = Label(w1, text = "수강과목")
    content = Label(w1, text = "수강내용")
    cost = Label(w1, text = "수강비용")
    member = Label(w1, text = "수강가능인원")
    
    id_input = Entry(w1, width = 10)
    classes_input = Entry(w1, width = 10)
    content_input = Entry(w1, width = 10)
    cost_input = Entry(w1, width = 10)
    member_input = Entry(w1, width = 10)
    insert = Button(w1, text = "입력", command = class_insert)
    
    id.pack()
    id_input.pack()
    classes.pack()
    classes_input.pack()
    content.pack()
    content_input.pack()
    cost.pack()
    cost_input.pack()
    member.pack()
    member_input.pack()  
    insert.pack()
    
    w1.mainloop()
    w1.destroy()
    
def class_insert():
    
    id = id_input.get()
    classes = classes_input.get()
    content = content_input.get()
    cost = cost_input.get()
    member = member_input.get()
    insert(id,classes,content,cost,member)

def printall_infor():
    
    w2 = Tk()
    
    w2.geometry("300x300")
    w2.title("수강정보전체출력")
    
    row = printall()

    row1 = Label(w2, text = row[0])
    row2 = Label(w2, text = row[1])
    row3 = Label(w2, text = row[2])

    row1.pack()
    row2.pack()
    row3.pack()

    w2.mainloop()

    
def update_infor():
    
    global id_input, cost_input
    
    w = Tk()

    w.geometry("300x300")
    w.title("수정")
    
    id = Label(w, text = "수강아이디")
    cost = Label(w, text = "수강비용")
    
    id_input = Entry(w, width = 10)
    cost_input = Entry(w, width = 10)
    
    update = Button(w, text = "수정", command = class_update)
    
    id.pack()
    id_input.pack()
    cost.pack()
    cost_input.pack()
    update.pack()
    
    w.mainloop()

def arrange_result():
    
    w = Tk()

    w.geometry("300x300")
    w.title("정리")
    
    data = arrange()
    sum = data[0][3] + data[1][3] + data[2][3]
    avg = sum / 3 
    
    info1 = Label(w, text = sum)
    info2 = Label(w, text = avg)
     
    info1.pack()
    info2.pack()

    w.mainloop()
    
def class_update():
    
    id = id_input.get()
    cost = cost_input.get()
    update(id,cost)
    

    
    