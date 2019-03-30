from tkinter import *

window = Tk()

def MakeLabelN():
    num = int(s1.get())
    for x in range(num):
        Label(window, text="Made label").pack()

s1 = Spinbox(window, from_=0, to=10, width=5) # form_ to n~n 까지 얼마나값이 오르고 내리는지 
s1.pack()

b1 = Button(window, text="Make label n", command=MakeLabelN)
b1.pack()

window.mainloop()