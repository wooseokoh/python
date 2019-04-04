from tkinter import *

def call(inputData):
    print("입력받은 값: " ,inputData)
    w = Tk()
    colors = ["green", "red", "orange", "white", "yellow", "blue"]
    print(len(colors), "개의 리스트 항목이 들어있음.")
    print(colors[0])
    
    r = 0
    
    for c in colors:
        print(c)
        l = Label(w, text = c, width = 15)
        l.grid(row = r, column = 0)
        
        b = Button(w, text = c, width = 15)
        b.grid(row = r, column = 0)
        r = r + 1
        
    w.mainloop()
    
