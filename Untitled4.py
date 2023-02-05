from tkinter import *
from PIL import Image, ImageTk
import random


root = Tk()
root.geometry('600x400+500+300')

var = StringVar()


def click():
    pass

pic_frame = Frame(root)
pic_frame.place(x=0, y=0)


image1 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp1.png")
test = ImageTk.PhotoImage(image1)

pic = Label(pic_frame, image=test)
pic.pack()

count_frame = Frame(root)
count_frame.place(x=400, y=50)

lab = Label(count_frame, textvariable=var)
lab.pack()


butt_frame = Frame(root)
butt_frame.place(x=400, y=200)

butt = Button(butt_frame, text="click", command=click)
butt.pack()


root.mainloop()