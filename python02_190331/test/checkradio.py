from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

window = Tk()

def ShowMsgs():
    showinfo("Message", "Clicked")
st1 = StringVar() #변수를 문자열로 출력 체크버튼일경우 StringVar() 사용
st2 = StringVar()
st3 = IntVar()

c1 = Checkbutton(window, text="Check1", variable=st1, command=ShowMsgs)
c1.grid(row=0, column=0)

c2 = Checkbutton(window, text="Check2", variable=st2, command=ShowMsgs)
c2.grid(row=0, column=1)

for x in range(2):
    r1 = Radiobutton(window, text="Radio"+str(x), variable=st3, value=x, command=ShowMsgs)
    r1.grid(row=1, column=x)
    
window.mainloop()


