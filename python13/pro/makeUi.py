from tkinter import *

w = Tk()

w.geometry("500x500")
w.title("PC방선불기")

id = Label(w, text = "아이디입력", font=("굴림", 10))
id_input = Entry(w, font=("굴림", 10), width = 10)


pw = Label(w, text = "비밀번호입력", font=("굴림", 10))
pw_input = Entry(w, font=("굴림", 10), width = 10)

login = Button(w, text="로그인")
naver = Button(w, text="네이버로그인")
# join = Button(w, text="회원가입", font=("굴림", 10), command = insert_infor)
serchid = Button(w, text="아이디찾기")
serchpw = Button(w, text="비밀번호찾기")

id.pack()
id_input.pack()

pw.pack()
pw_input.pack()

login.pack()
naver.pack()
# join.pack()
serchid.pack()
serchpw.pack()

# join.place(x = 100, y= 200)
serchid.place(x = 200, y= 200)
serchpw.place(x = 300, y= 200)

w.mainloop()




