from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.geometry('1100x400+500+300')
world_frame = Frame(root)
world_frame.grid()


image1 = Image.open("C:/Users/windowsux/Desktop/portal_small.png")
test = ImageTk.PhotoImage(image1)



butt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

left = Label(world_frame, image=test)
left.grid(row=0, column=0)



m_frame = Frame(root)
m_frame.grid(row=0, column=1)

lab1 = Label(m_frame, padx=4, pady=6, bg='green', text='hello')
lab1.grid(row=0, column=0)
lab2 = Label(m_frame, padx=4, pady=6,  bg='yellow', text='hello')
lab2.grid(row=1, column=0)
but1 = Button(m_frame, padx=4, pady=4, bg='green', text='hello')
but1.grid(row=2, column=0)
lab2 = Button(m_frame, padx=4, pady=4, bg='yellow', text='hello')
lab2.grid(row=3, column=0)

r_frame = Frame(root)
r_frame.grid(row=0, column=3)


varRow = 2
varColumn = 0

for button in butt:
    command = lambda x=button: select(x)
    Button(r_frame, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    
    varColumn += 1
    if varColumn > 7 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 6:
        varColumn = 0
        varRow += 1

lab3_frame = Frame(root)
lab3_frame.grid(row=1, column=3)

lab3 = Label(lab3_frame, padx=4, pady=6,  bg='yellow', text='Used letters:')
lab3.grid(row=0, column=0)
lab4 = Label(lab3_frame, padx=4, pady=6,  bg='yellow', text='A list of used attempts')
lab4.grid(row=0, column=1)

word_frame = Frame(root)
word_frame.grid(row=2, column=3)

word = Label(word_frame, padx=4, pady=6,  bg='yellow', text='__ __ __ __ __ __')
word.grid(row=0, column=0)




root.mainloop()