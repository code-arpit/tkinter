from tkinter import *

root = Tk()

entry_ = Entry(root, width=50)
entry_.pack()
entry_.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello " + entry_.get()
    mylabel = Label(root , text =hello)
    mylabel.pack()

mybutton = Button(root, text="Submit", padx=50, pady=20, command=myClick)
mybutton.pack()


root.mainloop()
