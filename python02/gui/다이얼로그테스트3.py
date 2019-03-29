from tkinter import *


def calplus():
    n1 = int(data.get())
    n2 = int(data1.get())
    plus = n1 + n2
    print("두수의 합은",plus)
def calmiu():
    n1 = int(data.get())
    n2 = int(data1.get())
    miu = n1 - n2
    print("두수의 차은",miu)
def calmul():
    n1 = int(data.get())
    n2 = int(data1.get())
    mul = n1 * n2
    print("두수의 곱은",mul)
def caldiv():
    n1 = int(data.get())
    n2 = int(data1.get())
    div = n1 / n2
    print("두수의 나눔은",div)

w = Tk()


num = Label(text = "첫번쨰 숫자 입력하세요")
num.pack()

data = Entry(w)
data.pack()

num = Label(text = "두번쨰 숫자를 입력하세요")
num.pack()

data1 = Entry(w)
data1.pack()

btn = Button(w, text = "+", command=calplus)
btn.pack()

btn = Button(w, text = "-", command=calmiu)
btn.pack()

btn = Button(w, text = "*", command=calmul)
btn.pack()

btn = Button(w, text = "/", command=caldiv)
btn.pack()



















w.mainloop()