from tkinter import *
from db.dbTest import *

def eventProcess():
    
    print("이벤트 처리 되었음")
    global name,id,tel,addr
    name = name_input.get()
    id = id_input.get()
    tel = tel_input.get()
    addr = addr_input.get()
    db_insert(name,id,tel,addr)
#   print("당신이 입력한 id :",id)

    
w = Tk()

w.geometry("380x500")
w.title("나의 첫 윈도우")
w.configure(bg = "green")

name = Label(w, text = "아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
id = Label(w, text = "패스워드 입력", font=("굴림",30), fg = "lightblue4",bg = "green")
tel = Label(w, text = "이름 입력", font=("굴림",30), fg = "gray32", bg = "green")
addr = Label(w, text = "전화번호 입력", font=("굴림",30), fg = "orchid2", bg = "green")
insert = Button(w, text="회원가입 처리", font=("궁서", 30), fg = "orange",  bg = "green", command = eventProcess) # command = eventProcess() ()가 안들어감

name_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10) # 영문자 10글자, 한글은 이보다 적게 들어감
id_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)
tel_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)
addr_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)

name.pack()
name_input.pack()
id.pack()
id_input.pack()
tel.pack()
tel_input.pack()
addr.pack()
addr_input.pack()
insert.pack()

w.mainloop()
    

    

