from tkinter import *

root = Tk()

def myClick():
    mylabel = Label(root , text ="i click")
    mylabel.pack()

mybutton = Button(root, text="click me", padx=50, pady=20, command=myClick, bg="red")
mybutton.pack()



root.mainloop()