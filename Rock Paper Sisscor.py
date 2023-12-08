import tkinter as tk
from tkinter import PhotoImage
import random

def rbutton_click():
    global cchoice
    global res
    lis = [1, 2, 3]
    num = random.choice(lis)
    lis1 = ["ROCK","PAPER","SISSCOR"]
    cchoice = "COMPUTER SELECTED " + lis1[num - 1]
    if num == 1:
        res = "DRAW"
    elif num == 2:
        res = "COMPUTER WINS"
    else:
        res = "YOU WIN"
    yourchoice.config(text="YOU SELECT ROCK")
    computerschoice.config(text=cchoice)
    final.config(text=res)

def pbutton_click():
    global cchoice
    global res
    lis = [1, 2, 3]
    num = random.choice(lis)
    lis1 = ["ROCK","PAPER","SISSCOR"]
    cchoice = "COMPUTER SELECTED " + lis1[num - 1]
    if num == 1:
        res = "YOU WIN"
    elif num == 2:
        res = "DRAW"
    else:
        res = "COMPUTER WINS"
    yourchoice.config(text="YOU SELECT PAPER")
    computerschoice.config(text=cchoice)
    final.config(text=res)

def sbutton_click():
    global cchoice
    global res
    lis = [1, 2, 3]
    num = random.choice(lis)
    lis1 = ["ROCK","PAPER","SISSCOR"]
    cchoice = "COMPUTER SELECTED " + lis1[num - 1]
    if num == 1:
        res = "COMPUTER WINS"
    elif num == 2:
        res = "YOU WIN"
    else:
        res = "DRAW"
    yourchoice.config(text="YOU SELECT SISSCOR")
    computerschoice.config(text=cchoice)
    final.config(text=res)

root = tk.Tk()
root.title("Rock Paper Scissor")

heading = tk.Label(root, text="ROCK PAPER SCISSOR", font=('Arial', 30, 'bold'))
heading.grid(row=0, column=1, pady=10, columnspan=3)

space = tk.Label(root, text=" ")
space.grid(row=1, column=1)

ins = tk.Label(root, text="SELECT YOUR CHOICE", font=('Arial', 20, 'bold'))
ins.grid(row=2, column=1, columnspan=3)


rpath = "rock.png"
rphoto = PhotoImage(file=rpath)
rbutton = tk.Button(root, image=rphoto, command=rbutton_click)
rbutton.grid(row=3, column=0, padx=10)
rock = tk.Label(root, text="ROCK",font=('Arial', 16, 'bold'))
rock.grid(row=4, column=0, padx=10, pady=10)


ppath = "paper.png"
pphoto = PhotoImage(file=ppath)
pbutton = tk.Button(root, image=pphoto, command=pbutton_click)
pbutton.grid(row=3, column=1, padx=10)
paper = tk.Label(root, text="PAPER",font=('Arial', 16, 'bold'))
paper.grid(row=4, column=1, padx=10, pady=10)


spath = "sisscor.png"
sphoto = PhotoImage(file=spath)
sbutton = tk.Button(root, image=sphoto, command=sbutton_click)
sbutton.grid(row=3, column=2, padx=10)
scissor = tk.Label(root, text="SCISSOR",font=('Arial', 16, 'bold'))
scissor.grid(row=4, column=2, padx=10, pady=10)

space1 = tk.Label(root,text=" ",font=('Arial', 16, 'bold'))
space1.grid(row=14,column=0)

yourchoice = tk.Label(root,text=" ",font=('Arial', 16, 'bold'))
yourchoice.grid(row=15,column=0,columnspan=3)

computerschoice = tk.Label(root, text=" ",font=('Arial', 16, 'bold'))
computerschoice.grid(row=16, column=0, columnspan=3)

final = tk.Label(root, text=" ",font=('Arial', 16, 'bold'))
final.grid(row=17, column=0, columnspan=3)

root.mainloop()
