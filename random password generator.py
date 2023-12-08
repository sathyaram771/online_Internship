import random
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="black")

difficulty = ""
ipath = "download.png"

iphoto = PhotoImage(file=ipath)
image = tk.Label(root,image=iphoto)
image.pack()

def Generate():
    try:
        noofcharacters = noofchar.get()
        print(noofcharacters.isnumeric())
        print(noofcharacters)
        no = int(noofcharacters)
        global easy
        global medium
        global hard
        if no >= 8 and noofcharacters.isnumeric():
            mlis = [lis1, lis2]
            h = random.sample(mlis, 1)
            print(h)
            word = ''.join(random.sample(h[0], no - 3))
            number = ''.join(random.sample(lis4, 3))
            easy = word + number
            i = lis1 + lis2
            word1 = ''.join(random.sample(i, no - 4))
            spl = ''.join(random.sample(lis3, 1))
            num = ''.join(random.sample(lis4, 3))
            medium = word1 + spl + num
            j = lis1 + lis2 + lis3 + lis4
            hard = ''.join(random.sample(j, no))
            global password
            password = ""
            print(difficulty)
            if difficulty == "easy":
                password += easy
            elif difficulty == "medium":
                password += medium
            elif difficulty == "hard":
                password += hard
            else:
                password += "Please Select the Complexity option"
            passw.config(text="THE REQUIRED PASSWORD: "+password, fg="white")
        else:
            passw.config(text="PLEASE MAKE SURE THAT THE NUMBER OF CHARACTERS IS MORE THAN EIGHT OR MAKE SURE YOU ENTERED A VALID INTEGER")
    except:
        passw.config(text="Please Enter all the Fields with appropriate value")

def on_select(event):
    selected_value = combobox.get()
    global difficulty
    difficulty = selected_value[::1]

heading = tk.Label(root, text="RANDOM PASSWORD GENERATOR", font=('Bold', 30), bg="black", fg="white")
heading.pack()

space = tk.Label(root, text=" ", bg="black")
space.pack()

noofcharLabel = tk.Label(root, text="ENTER THE NUMBER OF CHARACTERS", font=('Bold', 17), bg="black", fg="white")
noofcharLabel.pack()

noofchar = tk.Entry(root, font=('Bold', 17), bg="black", fg="white", insertbackground="white")  # Set text and cursor color
noofchar.pack()


s = tk.Label(root,text=" ",bg="black",fg="white")
s.pack()
options = ["easy", "medium", "hard"]

msg = tk.Label(root,text="SELECT THE COMPLEXITY",bg="black",fg="white",font=('Bold',17))
msg.pack()

style = ttk.Style()
style.configure('Custom.TCombobox', background='black', foreground='white', selectbackground='black', selectforeground='white')

combobox = ttk.Combobox(root, values=options ,font=('Bold', 17), style='Custom.TCombobox')
combobox.set("SELECT THE COMPLEXITY")
combobox.bind("<<ComboboxSelected>>", on_select)
combobox.pack()

lis1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lis2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lis3 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '"', ',', '.', '/', '\\', '<', '>', '?', '~']
lis4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

e = tk.Label(root,text=" ",bg="black",fg="white")
e.pack()

button = tk.Button(root, text="Generate", command=Generate, font=('Bold', 17), bg="white", fg="black", activebackground="black", activeforeground="white")
button.pack()

space1 = tk.Label(root, text=" ", bg="black")
space1.pack()

passw = tk.Label(root, text=" ", font=('Bold', 17), bg="black", fg="white")
passw.pack()

root.mainloop()
