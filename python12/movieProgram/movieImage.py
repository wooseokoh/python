from tkinter import *
from tkinter.messagebox import *

label = None

def img_change():
    global label
    icon = PhotoImage(file="m1.PNG")
    label['image'] = icon

if __name__ == '__main__':
    
    w =Tk()
    icon =PhotoImage(file = "web.PNG")
    label = Label(w, image=icon)
    button = Button(w, text="나를 눌러요...", command = img_change)
    
    label.pack()
    button.pack()
    showinfo("여기는 제목.부분", "여기는 출력내용 보이는곳.....")   
    showinfo("나는 메시지 박스...", "출력은 여기에 보여요")   
    w.mainloop()