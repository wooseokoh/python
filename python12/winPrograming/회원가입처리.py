from tkinter import *
from winPrograming.나의윈도우3 import insert_ui, delete_ui, update_ui, select_ui, select_all_ui



if __name__ == '__main__':
    
    w = Tk()
    
    w.geometry("500x500")
    w.title("나의 윈도우")

    
    insert = Button(w, text="회원가입 처리", font=("궁서", 30), fg = "orange",  bg = "green", command = insert_ui)
    delete = Button(w, text="회원가입 삭제", font=("궁서", 30), fg = "orange",  bg = "green", command = delete_ui)
    update = Button(w, text="회원가입 수정", font=("궁서", 30), fg = "orange",  bg = "green", command = update_ui)  
    select = Button(w, text="회원가입 선택", font=("궁서", 30), fg = "orange",  bg = "green", command = select_ui)
    select_all = Button(w, text="회원가입 모두선택", font=("궁서", 30), fg = "orange",  bg = "green", command = select_all_ui)
    
    insert.pack()
    delete.pack()
    update.pack()
    select.pack()
    select_all.pack()

    
    w.mainloop()
    








