from tkinter import* 
from tkinter import messagebox


# 7
def onClick():
    data1 = text.get()
    messagebox.showinfo("입력받은값", data1)  # 5
    print("입력받은값", data1)

# Tk() 화면 출력 1
window = Tk()

# 3
name = Label(window, text = "이름을 입력하세요")
name.pack()

# 4
text = Entry(window)
text.pack()

#버튼 생성 후 빈화면에 얹기 2 , 6
btn = Button(window,text = "입력버튼", command = onClick)
btn.pack()


window.mainloop()