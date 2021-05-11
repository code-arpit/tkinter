from tkinter import *

root = Tk()

entry_ = Entry(root, width=50)
entry_.pack()
entry_.insert(0, "Enter your name: ")

def myClick():
    mylabel = Label(root , text =entry_.get())
    mylabel.pack()

mybutton = Button(root, text="Enter your name", padx=50, pady=20, command=myClick)
mybutton.pack()



root.mainloop()