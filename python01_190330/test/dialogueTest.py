from tkinter import* # GUI 구현 가능한 모듈
from tkinter import messagebox

# 함수를 만들고 엔트리에 입력값을 받아서 버튼을 누르면 메세지 화면과 콘솔에 출력
def onClick():
    data1 = text.get() # 변수에 엔트리 값을 넣는다
    print("입력받은값", data1) # 콘솔에서 출력
    messagebox.showinfo("입력받은값", data1) # 메세지 화면의 제목
    text.delete(0,END) # 엔트리에 있는 것을 지워준다
    text.insert(0,"홍길동") # 엔트리에 값을 넣어준다
    
window = Tk()
  
# 그냥 텍스트 생성 후 화면에 고정
Label(window, text = "이름을 입력하세요").pack()

# 입력이 가능한 창 생성하고 화면에 고정
text = Entry(window)
text.pack()

# 버튼을 생성하고 화면에 고정
btn = Button(window, text = "입력버튼", command = onClick)
btn.pack()

window.mainloop()