from tkinter import *
import random

root = Tk()
root.geometry('1100x400+500+300')

def select(value):
    global guess
    guess = value
    print(guess)
    var_select.set(guess)

def play_again():
    global rando
    rando = random.choice(word_list)
    dash = len(rando)
    rando_word.set('__ ' *dash )

def play():
    play_again()

def enter():
    global guess
    if guess in rando:
        print('yes')
    else:
        print('nope')



rando_word = StringVar()
var_select = StringVar()

word_list = ['banana', 'devon', 'cat', 'look', 'whaaaaat']

butt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

right = Frame(root, width=400, height=400, bg='blue')
right.place(x=600, y=0)
middle = Frame(root, width=200, height=400, bg='red')
middle.place(x=400, y=0)
left = Frame(root, width=400, height=400, bg='green')
left.place(x=0, y=0)
lab = Label(right, text='').grid(row=0, columnspan=1)
answer_frame = Frame(root, width=400, height=100, bg='yellow')
answer_frame.place(x=600, y=300)

your_choice = Label(middle, text='Selection', font=('Times', 24)).pack()
choice_entered = Label(middle, textvariable=var_select, font=('Times', 48)).pack()

answer_label = Label(answer_frame, height=1, bg='pink', textvariable=rando_word, font=('Times', 36)).grid(row=1, column= 0, sticky=S)

li = Label(left, text="left", width=4, height=1, font=('Times',28)).grid(row=2, column=0)

enter_butt = Button(middle, text='Enter', command=enter).pack(pady=20, padx=20)
play_butt = Button(middle, text='Play', command=play_again).pack(pady=20, padx=20)



varRow = 2
varColumn = 0

for button in butt:
    command = lambda x=button: select(x)
    Button(right, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    # if butt == "clear":
    #     Button(right, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    # if butt == "return":
    #     Button(right, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)



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


root.mainloop()