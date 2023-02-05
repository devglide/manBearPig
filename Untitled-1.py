from tkinter import *
import tkFileDialog
from tkFileDialog import askdirectory
from PIL import  Image
from PIL import Image, ImageTk

class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.choose)
        self.choose = Label(self, text="Choose file").pack()
        self.image = PhotoImage(file='cualitativa.gif')
        self.label = Label(image=self.image)


        self.file.pack()
        self.label.pack()

    def choose(self):
        ifile = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        path = ifile.name
        self.image2 = PhotoImage(file="C:/Users/windowsux/Desktop/mbp/mbp1.png")
        self.label.configure(image=self.image2)
        self.label.image=self.image2


root = Tk()
app = GUI(master=root)
app.mainloop()
root.destroy()


# import tkinter as tk
# from PIL import Image, ImageTk


# root = tk.Tk()

# img = ImageTk.PhotoImage(Image.open("C:/Users/windowsux/Desktop/mbp/mbp1.png"))
# panel = tk.Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")

# def callback(event):
#     img2 = ImageTk.PhotoImage(Image.open("C:/Users/windowsux/Desktop/mbp/mbp2.png"))
#     panel.configure(image=img2)
#     panel.image = img2

# root.bind("<Return>", callback)
# root.mainloop()