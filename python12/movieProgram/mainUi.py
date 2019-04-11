from tkinter import *
from movieProgram.movieUi import insert_infor, update_infor, delete_infor



if __name__ == '__main__':
    
    w = Tk()
    
    w.geometry("500x500")
    w.title("나의 윈도우")

    insert = Button(w, text="회원가입 처리", font=("궁서", 30), command = insert_infor)
    update = Button(w, text="회원가입 수정", font=("궁서", 30), command = update_infor)
    delete = Button(w, text="회원가입 삭제", font=("궁서", 30), command = delete_infor)

    insert.pack()
    update.pack()
    delete.pack()

    w.mainloop()
    