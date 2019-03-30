from tkinter import* # GUI 구현 가능한 모듈

window = Tk()
  
def correctPassword():
    pw = str(text.get())
    if (pw =="abc123"):
    ace = Label(window, text = "correct")
    ace.pack()
    btn.config(state = "disabled")
    
# 그냥 텍스트 생성 후 화면에 고정
name = Label(window, text = "Entry")
name.pack()

# 입력이 가능한 창 생성하고 화면에 고정
text = Entry(window)
text.pack()


btn = Button(window, text = "Correct Password?", command = correctPassword)
btn.pack()

window.mainloop()
