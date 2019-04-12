from tkinter import *
from movieProgram.movieDb import *

id_input, title_input, content_input, director_input, img_input = None,None,None,None,None
data, record = None,None

def movie_insert():
    
    print("이벤트 처리 되었음")

    id = id_input.get()
    title = title_input.get()
    content = content_input.get()
    director = director_input.get()
    img = img_input.get()
    db_insert(id,title,content,director,img)
    
def movie_update():
    
    print("이벤트 처리 되었음")
    
    id = id_input.get()
    title = title_input.get()
    content = content_input.get()
    director = director_input.get()
    img = img_input.get()
    db_update(id,title,content,director,img)

def movie_delete():
    
    print("이벤트 처리 되었음")

    id = id_input.get()
    db_delete(id)
    
def movie_select():
    
    global data,record
    
    print("정보검색시작")
    id = data.get()
    record = db_select(id)
    select_result_infor(record)

    
def insert_infor():
    
    global id_input, title_input, content_input, director_input, img_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("영화입력")
    w.configure(bg = "green")
    
    
    id = Label(w, text = "아이디 입력", font=("굴림",20))
    title = Label(w, text = "제목 입력", font=("굴림",20))
    content = Label(w, text = "만족도 입력", font=("굴림",20))
    director = Label(w, text = "감독 입력", font=("굴림",20))
    img = Label(w, text = "이미지 입력", font=("굴림",20))
    insert = Button(w, text="회원가입 처리", font=("궁서", 20), fg = "orange",  bg = "green", command = movie_insert)
    
    id_input = Entry(w, font=("굴림", 20), width = 10)
    title_input = Entry(w, font=("굴림", 20), width = 10)
    content_input = Entry(w, font=("굴림", 20), width = 10)
    director_input = Entry(w, font=("굴림", 20), width = 10)
    img_input = Entry(w, font=("굴림", 20), width = 10)            

    id.pack()
    id_input.pack()
    title.pack()
    title_input.pack()
    content.pack()
    content_input.pack()
    director.pack()
    director_input.pack()
    img.pack()
    img_input.pack()
    insert.pack()

    w.mainloop()

def update_infor():
    
    global id_input, title_input, content_input, director_input, img_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("영화수정")
    w.configure(bg = "green")
    
    id = Label(w, text = "아이디 입력", font=("굴림",30))
    title = Label(w, text = "제목 입력", font=("굴림",30))
    content = Label(w, text = "만족도 입력", font=("굴림",30))
    director = Label(w, text = "감독 입력", font=("굴림",30))
    img = Label(w, text = "이미지 입력", font=("굴림",30))
    insert = Button(w, text="회원수정", font=("궁서", 30), fg = "orange",  bg = "green", command = movie_update)
    
    id_input = Entry(w, font=("굴림", 30), width = 10)
    title_input = Entry(w, font=("굴림", 30), width = 10)
    content_input = Entry(w, font=("굴림", 30), width = 10)
    director_input = Entry(w, font=("굴림", 30), width = 10)
    img_input = Entry(w, font=("굴림", 30), width = 10)
    
    id.pack()
    id_input.pack()
    title.pack()
    title_input.pack()
    content.pack()
    content_input.pack()
    director.pack()
    director_input.pack()
    img.pack()
    img_input.pack()
    insert.pack()
    
    w.mainloop()
    
def delete_infor():
    
    global id_input
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("영화삭제")
    w.configure(bg = "green")
    
    id = Label(w, text = "아이디 입력", font=("굴림",30))
    insert = Button(w, text="회원삭제", font=("궁서", 30), command = movie_delete) 
    
    id_input = Entry(w, font=("굴림", 30), width = 10)

    id.pack()
    id_input.pack()

    insert.pack()
    
    w.mainloop()
    
def select_infor():
    
    global data
    
    w = Tk()
    
    w.geometry("380x500")
    w.title("영화정보")
    w.configure(bg = "green")

    intro = Label(w, text="검색할 ID를 입력하세요. :", font=("궁서", 10), width = 30)
    data = Entry(w, font=("궁서", 10), width = 10)
    start = Button(w, text="영화정보 검색", command = movie_select)
    
    intro.pack()
    data.pack()
    start.pack()

    w.mainloop()

def select_result_infor(record):
    
    global id_input, title_input, content_input, director_input, img_input
    
    w = Toplevel()
    
    w.geometry("380x1000")
    w.title("모든영화정보")
    w.configure(bg = "blue")

    id = Label(w, text = "검색된 아이디", font=("굴림",30))
    title = Label(w, text = "검색된 제목", font=("굴림",30))
    content = Label(w, text = "검색된 만족도", font=("굴림",30))
    director = Label(w, text = "검색된 감독", font=("굴림",30))
    img = Label(w, text = "검색된 이미지", font=("굴림",30))
    
    id_input = Label(w, text=record[0], font=("궁서", 30))
    title_input = Label(w, text=record[1], font=("궁서", 30))
    content_input = Label(w, text=record[2], font=("궁서", 30))
    director_input = Label(w, text=record[3], font=("궁서", 30))

    icon = PhotoImage(file = record[4])
    
    img_input = Label(w)
    img_input.configure(image=icon)
    img_input.image = icon
    
    id.pack()
    id_input.pack()
    title.pack()
    title_input.pack()
    content.pack()
    content_input.pack()
    director.pack()
    director_input.pack()
    img.pack()
    img_input.pack()
    
    w.mainloop()
    
def select_all_infor():
    pass

def image_i():
    pass

    
