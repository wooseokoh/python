from tkinter import *

def process():
    d2 = int(data2.get())
    age = 2019 - d2 + 1
    print(age)
    result["text"] = "나이는 " + str(age)

w = Tk()

# 1. 이름 입력 (라벨 + 입력란)
name = Label(w, text = "이름을 입력하세요..." )
name.pack()
data1 = Entry(w)
data1.pack()

# 2. 태어난 해 입력
year = Label(w, text = "태어난 해를 입력하세요..." )
year.pack()

data2 = Entry(w)
data2.pack()

# 3. 버튼 처리
btn = Button(w, text = "나를 눌러요...", command=process)
btn.pack()

result = Label(w, text = "여기에 나이 출력" )
result.pack()






w.mainloop()