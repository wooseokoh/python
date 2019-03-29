from tkinter import* 


def test():
    data1 = text.get()
    print("이름을 입력하세요", data1)
    

def test1():
    data2 = int(text1.get())
    age = 2019 - data2 + 1
    print("나이는", age)
    result["text"] = "나이는" + str(age)

w = Tk()

name = Label(w, text = "이름을 입력하세요")
name.pack()

text = Entry(w)
text.pack()

btn = Button(w,text = "입력버튼", command = test)
btn.pack()

year = Label(w, text = "태어난해를 입력하세요")
year.pack()

text1= Entry(w)
text1.pack()

btn = Button(w,text = "입력버튼", command = test1)
btn.pack()


btn = Button(w,text = "나를 눌러주세요", command = test1)
btn.pack()


w.mainloop()



