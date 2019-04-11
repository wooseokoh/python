from tkinter import *
from db.dbTest import *

record, name_input, id_input, tel_input, addr_input, data = None,None,None,None,None,None


def eventProcess_insert():
    
    print("이벤트 처리 되었음")

    name = name_input.get()
    id = id_input.get()
    tel = tel_input.get()
    addr = addr_input.get()
    db_insert(name,id,tel,addr)
#   print("당신이 입력한 id :",id)

def eventProcess_delete():
    
    print("이벤트 처리 되었음")

    name = name_input.get()
    db_delete(name)


def eventProcess_update():
    
    print("이벤트 처리 되었음")
    name = name_input.get()
    tel = tel_input.get()
    db_update(name, tel)

def eventProcess_select():
    
    global data,record
    
    print("정보검색시작")
    name = data.get()
    record = db_select(name) # 튜플값이 들어옴
    select_result_ui(record)


def delete_ui():
    
    global name_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("나의 첫 윈도우")
    w.configure(bg = "green")
    
    name = Label(w, text = "아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
    insert = Button(w, text="회원삭제", font=("궁서", 30), fg = "orange",  bg = "green", command = eventProcess_delete) 
    
    name_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10) # 영문자 10글자, 한글은 이보다 적게 들어감

    
    name.pack()
    name_input.pack()

    insert.pack()
    
    w.mainloop()
    
    
def update_ui():
    
    global name_input, tel_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("나의 첫 윈도우")
    w.configure(bg = "green")
    
    name = Label(w, text = "아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
    tel = Label(w, text = "이름 입력", font=("굴림",30), fg = "gray32", bg = "green")
    insert = Button(w, text="회원수정", font=("궁서", 30), fg = "orange",  bg = "green", command = eventProcess_update)
    
    name_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10) # 영문자 10글자, 한글은 이보다 적게 들어감
    tel_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)
    
    name.pack()
    name_input.pack()
    tel.pack()
    tel_input.pack()
    insert.pack()
    
    w.mainloop()
    
def select_ui():
    
    global data
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("나의 첫 윈도우")
    w.configure(bg = "green")
    
    intro = Label(w, text="검색할 ID를 입력하세요. :", font=("궁서", 30), fg = "orange",  bg = "green", width = 30)
    data = Entry(w, font=("궁서", 30), fg="red", bg="yellow", width=12)
    start = Button(w, text="회원정보 검색", font=("궁서", 20), fg="red", bg="yellow", command=eventProcess_select)
    
    intro.pack()
    data.pack()
    start.pack()
    
    w.mainloop()

def select_result_ui(record):
    
    global name_input, id_input, tel_input, addr_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("나의 첫 윈도우")
    w.configure(bg = "blue")
    
    name = Label(w, text = "검색된 아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
    id = Label(w, text = "검색된 패스워드 입력", font=("굴림",30), fg = "lightblue4",bg = "green")
    tel = Label(w, text = "검색된 이름 입력", font=("굴림",30), fg = "gray32", bg = "green")
    addr = Label(w, text = "검색된 전화번호 입력", font=("굴림",30), fg = "orchid2", bg = "green")
    
    name_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
    id_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
    tel_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
    addr_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
    
    name.pack()
    name_input.pack()
    id.pack()
    id_input.pack()
    tel.pack()
    tel_input.pack()
    addr.pack()
    addr_input.pack()

    
    w.mainloop()

def select_all_ui():
    pass

def insert_ui():
    
    global name_input, id_input, tel_input, addr_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("나의 첫 윈도우")
    w.configure(bg = "green")
    
    name = Label(w, text = "아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
    id = Label(w, text = "패스워드 입력", font=("굴림",30), fg = "lightblue4",bg = "green")
    tel = Label(w, text = "이름 입력", font=("굴림",30), fg = "gray32", bg = "green")
    addr = Label(w, text = "전화번호 입력", font=("굴림",30), fg = "orchid2", bg = "green")
    insert = Button(w, text="회원가입 처리", font=("궁서", 30), fg = "orange",  bg = "green", command = eventProcess_insert) # command = eventProcess() ()가 안들어감
    
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
    
    
    
    
    