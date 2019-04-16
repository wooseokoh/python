def member_update():
    
    print("이벤트 처리 되었음")
    
    id = id_input.get()
    pw = pw_input.get()
    personalNum = personalNum_input.get()
    addr = addr_input.get()
    email = email_input.get()
    num = num_input.get()
    db_update(id,pw,personalNum,addr,email,num)

def member_delete():
    
    print("이벤트 처리 되었음")

    id = id_input.get()
    db_delete(id)
    
def member_select():
    
    global data,record
    
    print("정보검색시작")
    id = data.get()
    record = db_select(id)
    select_result_infor(record)


def update_infor():
    
    global id_input, pw_input, personalNum_input, addr_input, email_input, num_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("회원정보수정")
    w.configure(bg = "green")
    
    
    id = Label(w, text = "아이디 입력", font=("굴림",20))
    pw = Label(w, text = "비밀번호 입력", font=("굴림",20))
    personalNum = Label(w, text = "주민등록번호 입력", font=("굴림",20))
    addr = Label(w, text = "주소 입력", font=("굴림",20))
    email = Label(w, text = "이메일 입력", font=("굴림",20))
    num = Label(w, text = "전화번호입력", font=("굴림",20))
    insert = Button(w, text="회원정보수정 처리", font=("궁서", 20), fg = "orange",  bg = "green", command = member_update)
    
    id_input = Entry(w, font=("굴림", 20), width = 10)
    pw_input = Entry(w, font=("굴림", 20), width = 10)
    personalNum_input = Entry(w, font=("굴림", 20), width = 10)
    addr_input = Entry(w, font=("굴림", 20), width = 10)
    email_input = Entry(w, font=("굴림", 20), width = 10)
    num_input = Entry(w, font=("굴림", 20), width = 10)             

    id.pack()
    id_input.pack()
    pw.pack()
    pw_input.pack()
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
    
def delete_infor():
    
    global id_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("회원정보삭제")
    w.configure(bg = "green")
    
    id = Label(w, text = "아이디 입력", font=("굴림",30))
    insert = Button(w, text="회원삭제", font=("궁서", 30), command = member_delete) 
    
    id_input = Entry(w, font=("굴림", 30), width = 10)

    id.pack()
    id_input.pack()

    insert.pack()
    
    w.mainloop()
    

def select_result_infor(record):
    
    global id_input, pw_input, personalNum_input, addr_input, email_input
    
    w = Toplevel()
    
    w.geometry("380x1000")
    w.title("회원정보")
    w.configure(bg = "blue")

    id = Label(w, text = "검색된 아이디", font=("굴림",30))
    pw = Label(w, text = "검색된 패스워드", font=("굴림",30))
    personalNum = Label(w, text = "검색된 주민번호", font=("굴림",30))
    addr = Label(w, text = "검색된 주소", font=("굴림",30))
    email = Label(w, text = "검색된 이메일", font=("굴림",30))
    num = Label(w, text = "검색된 번호", font=("굴림",30))
    
    id_input = Label(w, text=record[0], font=("궁서", 30))
    pw_input = Label(w, text=record[1], font=("궁서", 30))
    personalNum_input = Label(w, text=record[2], font=("궁서", 30))
    addr_input = Label(w, text=record[3], font=("궁서", 30))
    email_input = Label(w, text=record[4], font=("궁서", 30))
    num_input = Label(w, text=record[5], font=("궁서", 30))

    id.pack()
    id_input.pack()
    pw.pack()
    pw_input.pack()
    personalNum.pack()
    personalNum_input.pack()
    addr.pack()
    addr_input.pack()
    email.pack()
    email_input.pack()
    num.pack()
    num_input.pack()
    
    w.mainloop()
    
def select_all_infor():
    pass

def image_i():
    pass


