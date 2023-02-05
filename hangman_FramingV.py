from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry('1100x400+500+300')

tries = 0

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
    global guess, tries
    if guess in rando:
        print('yes')
        guessed_letters.append(guess)
        letters_list.set(str(guessed_letters))
    else:
        print('nope')
        guessed_letters.append(guess)
        letters_list.set(guess)
        tries += 1
        window_state()
    print(guessed_letters)

def window_state():
    global back_drop, li
    if tries == 0:
        back_drop = test
    elif tries == 1:
        back_drop = test2
    elif tries == 2:
        back_drop = test3
    elif tries == 3:
        back_drop = test4
    elif tries == 4:
        back_drop = test5
    elif tries == 5:
        back_drop = test6
    else:
        back_drop = test7

image1 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp1.png")
test = ImageTk.PhotoImage(image1)

image2 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp2.png")
test2 = ImageTk.PhotoImage(image2)

image3 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp3.png")
test3 = ImageTk.PhotoImage(image3)

image4 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp4.png")
test4 = ImageTk.PhotoImage(image4)

image5 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp5.png")
test5 = ImageTk.PhotoImage(image5)

image6 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp6.png")
test6 = ImageTk.PhotoImage(image6)

image7 = Image.open("C:/Users/windowsux/Desktop/mbp/mbp7.png")
test7 = ImageTk.PhotoImage(image7)

guessed_letters = []

window_state()

rando_word = StringVar()
var_select = StringVar()
letters_list = StringVar()




word_list = ['banana', 'devon', 'cat', 'look', 'whaaaaat']
butt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

root.configure(bg='orange')





#Create Frames
left = Frame(root, width=400, height=400, bg='green')
left.place(x=0, y=0)
middle = Frame(root, width=200, height=400, bg='red')
middle.place(x=600, y=0)
right = Frame(root, width=400, height=400, bg='blue')
right.place(x=735, y=0)
guesses = Frame(root)
guesses.place(x=735, y=175)
answer_frame = Frame(root, width=400, height=100, bg='yellow')
answer_frame.place(x=600, y=300)

#Hangman 
li = Label(left, image=back_drop)
li.pack(side=RIGHT)




#Middle window
your_choice = Label(middle, text='Selection', font=('Times', 24)).pack()
choice_entered = Label(middle, textvariable=var_select, font=('Times', 48)).pack()
enter_butt = Button(middle, text='Enter', command=enter).pack(pady=20, padx=20)
play_butt = Button(middle, text='Play', command=play_again).pack(pady=20, padx=20)


#Keyboard window
guesses_lab = Label(guesses, text="Guessed:", font=('Times', 20)).grid(row=0, column=0, pady=25)
lab = Label(guesses, textvariable=letters_list).grid(row=0, column=1, pady=25)


#Hint window
answer_label = Label(answer_frame, height=1, bg='pink', textvariable=rando_word, font=('Times', 36)).grid(row=1, column= 0, sticky=S)


varRow = 2
varColumn = 0

for button in butt:
    command = lambda x=button: select(x)
    Button(right, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    
    varColumn += 1
    if varColumn > 5 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 5 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 5 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 5 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 5 and varRow == 6:
        varColumn = 0
        varRow += 1


root.mainloop()