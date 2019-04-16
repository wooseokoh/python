from tkinter import *
from preMachine.handlingDb import *
from tkinter import messagebox

id_input, pw_input, pw_re_input, name_input, personalNum_input, addr_input, email_input, num_input = None,None,None,None,None,None,None,None
data,data1,record = None,None,None
    
def member_insert():
    
    id = id_input.get()
    pw = pw_input.get()
    name = name_input.get()
    personalNum = personalNum_input.get()
    addr = addr_input.get()
    email = email_input.get()
    num = num_input.get()
    db_insert(id,pw,name,personalNum,addr,email,num)\
    
def duplCheck():
    
    for x in id: 
        if id_input == id:
            messagebox.showinfo("Error", "아이디를 다시 입력해주세요")
        else:
            messagebox.showinfo("Error", "이 아이디는 사용 가능합니다.")

     
def insert_infor():
    
    global id_input, pw_input, name_input, personalNum_input, addr_input, email_input, num_input, pw_re_input
    
    w = Tk()
    
    w.geometry("500x700")
    w.title("회원정보입력")    
        
    id = Label(w, text = "아이디 입력", font=("굴림",10))
    duplication = Button(w, text="중복체크", font=("궁서", 10), command = duplCheck)
    pw = Label(w, text = "비밀번호 입력", font=("굴림",10))
    pw_re = Label(w, text = "비밀번호 다시입력", font=("굴림",10))
    name = Label(w, text = "이름 입력", font=("굴림",10))
    personalNum = Label(w, text = "주민등록번호 입력", font=("굴림",10))
    addr = Label(w, text = "주소 입력", font=("굴림",10))
    email = Label(w, text = "이메일 입력", font=("굴림",10))
    num = Label(w, text = "전화번호입력", font=("굴림",10))
    insert = Button(w, text="회원가입 처리", font=("궁서", 10), command = member_insert)
        
    id_input = Entry(w, font=("굴림", 10), width = 10)
    pw_input = Entry(w, font=("굴림", 10), width = 10)
    pw_re_input = Entry(w, font=("굴림", 10), width = 10)
    name_input = Entry(w, font=("굴림", 10), width = 10)
    personalNum_input = Entry(w, font=("굴림", 10), width = 10)
    addr_input = Entry(w, font=("굴림", 10), width = 10)
    email_input = Entry(w, font=("굴림", 10), width = 10)
    num_input = Entry(w, font=("굴림", 10), width = 10)     

    id.pack()
    id_input.pack()
    duplication.pack()
    pw.pack()
    pw_input.pack()
    pw_re.pack()
    pw_re_input.pack()
    name.pack()
    name_input.pack()
    personalNum.pack()
    personalNum_input.pack()
    addr.pack()
    addr_input.pack()
    email.pack()
    email_input.pack()
    num.pack()
    num_input.pack()
    insert.pack()

    w.mainloop()
    
def member_select_id():
    
    global data,record
    
    print("정보검색시작")
    id = data.get() and data1.get()
    record = db_select_id(id)
    select_result_id(record)
    
def select_infor_id():
    
    global data,data1
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("아이디")

    intro = Label(w, text="이름을 입력하세요. :", font=("궁서", 10), width = 30)
    intro1 = Label(w, text="주민번호를 입력하세요. :", font=("궁서", 10), width = 30)
    data = Entry(w, font=("궁서", 10), width = 10)
    data1 = Entry(w, font=("궁서", 10), width = 10)
    start = Button(w, text="회원정보 검색", command = member_select_id)
    
    intro.pack()
    data.pack()
    intro1.pack()
    data1.pack()
    start.pack()

    w.mainloop()
    
def select_result_id(record):
    
    global id_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("아이디")

    id = Label(w, text = "검색된 아이디", font=("굴림",30))
    
    id_input = Label(w, text=record[0], font=("궁서", 30))

 
    id.pack()
    id_input.pack()


    w.mainloop()

def member_select_pw():
    
    global data,record
    
    print("정보검색시작")
    pw = data.get()
    record = db_select_pw(pw)
    select_result_pw(record)
    
def select_infor_pw():
    
    global data
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("비밀번호")


    intro = Label(w, text="ID를 입력하세요. :", font=("궁서", 10), width = 30)
    data = Entry(w, font=("궁서", 10), width = 10)
    start = Button(w, text="회원정보 검색", command = member_select_pw)
    
    intro.pack()
    data.pack()
    start.pack()

    w.mainloop()
    
def select_result_pw(record):
    
    global pw_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("비밀번호")

    pw = Label(w, text = "검색된 패스워드", font=("굴림",30))

    pw_input = Label(w, text=record[1], font=("궁서", 30))

    pw.pack()
    pw_input.pack()

    w.mainloop()
    



    
    