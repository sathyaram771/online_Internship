import tkinter as tk

a = 0
b = 0
result = 0

def pbutton_click():
    user_input = user_input_entry.get()
    global a
    a = int(user_input)
    user_input1 = user_input_entry1.get()
    global b
    b = int(user_input1)
    global result
    result = a + b

def mbutton_click():
    user_input = user_input_entry.get()
    global a
    a = int(user_input)
    user_input1 = user_input_entry1.get()
    global b
    b = int(user_input1)
    global result
    result = a * b

def sbutton_click():
    user_input = user_input_entry.get()
    global a
    a = int(user_input)
    user_input1 = user_input_entry1.get()
    global b
    b = int(user_input1)
    global result
    result = a - b

def dbutton_click():
    user_input = user_input_entry.get()
    global a
    a = int(user_input)
    user_input1 = user_input_entry1.get()
    global b
    b = int(user_input1)
    global result
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"

def display_content():
    fresult_label.config(text=str(result))

window = tk.Tk()
window.title("Calculator")

user_input_label = tk.Label(window, text="Enter first number:")
user_input_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

user_input_entry = tk.Entry(window)
user_input_entry.grid(row=0, column=1, padx=10, pady=10)

user_input_label1 = tk.Label(window, text="Enter second number:")
user_input_label1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

user_input_entry1 = tk.Entry(window)
user_input_entry1.grid(row=1, column=1, padx=10, pady=10)

pbutton = tk.Button(window, text="+", command=pbutton_click)
pbutton.grid(row=2, column=0, padx=10, pady=10)

mbutton = tk.Button(window, text="*", command=mbutton_click)
mbutton.grid(row=2, column=1, padx=10, pady=10)

sbutton = tk.Button(window, text="-", command=sbutton_click)
sbutton.grid(row=2, column=2, padx=10, pady=10)

dbutton = tk.Button(window, text="/", command=dbutton_click)
dbutton.grid(row=2, column=3, padx=10, pady=10)

fresult_label = tk.Label(window, text="", font=('Arial', 12))
fresult_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

fbutton = tk.Button(window, text="Calculate", command=display_content)
fbutton.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()
