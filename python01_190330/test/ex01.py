from tkinter import *

window = Tk()

t1 = Text(window,bg="powder blue")
t1.pack(side=LEFT)
t1.delete(0.0, END) # 엔트리 = 0,END 텍스트 = 0.0,END
t1.insert(END, "hello.")

window.mainloop()
