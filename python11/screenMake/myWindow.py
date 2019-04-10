from tkinter import *

def eventProcess():
    print("이벤트 처리 되었음")

w = Tk()

w.geometry("380x500")
w.title("나의 첫 윈도우")
w.configure(bg = "green")

id = Label(w, text = "아이디 입력", font=("굴림",30), fg = "cyan3",bg = "green")
pw = Label(w, text = "패스워드 입력", font=("굴림",30), fg = "lightblue4",bg = "green")
name = Label(w, text = "이름 입력", font=("굴림",30), fg = "gray32", bg = "green")
tel = Label(w, text = "전화번호 입력", font=("굴림",30), fg = "orchid2", bg = "green")
insert = Button(w, text="회원가입 처리", font=("궁서", 30), fg = "orange",  bg = "green", command = eventProcess)

id_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10) # 영문자 10글자, 한글은 이보다 적게 들어감
pw_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)
name_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)
tel_input = Entry(w, font=("굴림", 30), fg = "lightblue1", bg="pink", width = 10)

id.pack()
id_input.pack()
pw.pack()
pw_input.pack()
name.pack()
name_input.pack()
tel.pack()
tel_input.pack()
insert.pack()


w.mainloop()

