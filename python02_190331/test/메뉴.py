from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from random import randint

window = Tk()

menubar = Menu(window)

menuex = Menu(menubar, tearoff=0)
menuex.add_command(label="Quit", command=lambda:window.destroy())

menubar.add_cascade(label="File", menu=menuex)
menubar.add_cascade(label="Help")

def Carte():
    result = combo.get()
    ran = str(randint(1, 3))
    if result == ran:
        showinfo("WOW!", "Computer's number and your number\nis same!")      
    else:
        showinfo("Example", "You chose " + result + ",\nand computer chose " + ran + ".")

        
combo = Combobox(window, width=10)
combo["values"] = (1, 2, 3)
combo.grid(row=0, column=0, sticky=W)

b1 = Button(window, text="Click", width=5, command = Carte)
b1.grid(row=0, column=1, sticky=W)

window.config(menu=menubar)

window.mainloop()

