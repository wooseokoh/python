from tkinter import*
from tkinter.ttk import* # 콤보박스 생성 모듈
from random import randint # 랜덤함수 생성 모듈
from tkinter.messagebox import *

window = Tk()

def Carte():
    result = combo.get()
    ran = str(randint(1, 3))
    if result == ran:
        showinfo("WOW!", "Computer's number and your number\nis same!")      
    else:
        showinfo("Example", "You chose " + result + ",\nand computer chose " + ran + ".")

combo = Combobox(window, width=10)
combo["values"] = (1,2,3)
combo.grid(row=0, column=0, sticky=W)

b1 = Button(window, text="Click", width=5, command=Carte)
b1.grid(row=0, column=1, sticky=W)


window.mainloop()