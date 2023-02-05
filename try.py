from tkinter import *

root = Tk()
root.geometry('400x400+1500+300')

left = Frame(root).place(x=0, y=0)
right = Frame(root).place(x=200, y=0)

var = StringVar()

def select():
    var.set('a')

choice = Label(left, textvariable=var, font=("Times", 48)).grid(row=0, column=0)

a_choice = Button(right, text='a',  command=select).grid(row=0, column=0)





root.mainloop()