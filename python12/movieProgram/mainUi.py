from tkinter import *
from movieProgram.movieUi import insert_infor, update_infor, delete_infor, select_infor, select_all_infor



if __name__ == '__main__':
    
    w = Tk()
    
    w.geometry("500x500")
    w.title("나의 윈도우")

    insert = Button(w, text="영화 입력", font=("궁서", 30), command = insert_infor)
    update = Button(w, text="영화 수정", font=("궁서", 30), command = update_infor)
    delete = Button(w, text="영화 삭제", font=("궁서", 30), command = delete_infor)
    select = Button(w, text="영화 선택", font=("궁서", 30), command = select_infor)
    select_all = Button(w, text="영화 모두선택", font=("궁서", 30), command = select_all_infor)

    insert.pack()
    update.pack()
    delete.pack()
    select.pack()
    select_all.pack()

    w.mainloop()
    
