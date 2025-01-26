from tkinter import *
import math

window = Tk()
window.geometry("439x420")
window.title("Calculator")
window.resizable(False, False)

entry_output = StringVar()
entry_value = ''
entry = Entry(master=window, width=240,bg="#ccddff", textvariable=entry_output,font=("arial 28 bold"))
entry.place(x=0, y=0)

def show(value):
    global entry_value, entry_output
    entry_value += str(value)
    entry_output.set(entry_value)

def clear():
    global entry_value, entry_output
    entry_value = ''
    entry_output.set(entry_value)

def solve():
    global entry_value, entry_output
    result = eval(entry_value)
    entry_output.set(result)

area = 0

def mode():
    i = "enter radius?: "
    entry_output.set(i)
    radius = entry.get()[15:]
    area = math.pi * float(radius)**2


    





Button(master=window, width=11, height=4, text='(', relief='flat', bg='white', command=lambda: show("(")).place(x=0 , y=50)
Button(master=window, width=11, height=4, text=')', relief='flat', bg='white', command=lambda: show(")")).place(x=90 , y=50)
Button(master=window, width=11, height=4, text='%', relief='flat', bg='white', command=lambda: show("%")).place(x=180 , y=50)
Button(master=window, width=11, height=4, text='1', relief='flat', bg='white', command=lambda: show("1")).place(x=0 , y=125)
Button(master=window, width=11, height=4, text='2', relief='flat', bg='white', command=lambda: show("2")).place(x=90 , y=125)
Button(master=window, width=11, height=4, text='3', relief='flat', bg='white', command=lambda: show("3")).place(x=180 , y=125)
Button(master=window, width=11, height=4, text='4', relief='flat', bg='white', command=lambda: show("4")).place(x=0 , y=200)
Button(master=window, width=11, height=4, text='5', relief='flat', bg='white', command=lambda: show("5")).place(x=90 , y=200)
Button(master=window, width=11, height=4, text='6', relief='flat', bg='white', command=lambda: show("6")).place(x=180 , y=200)
Button(master=window, width=11, height=4, text='7', relief='flat', bg='white', command=lambda: show("7")).place(x=0 , y=275)
Button(master=window, width=11, height=4, text='8', relief='flat', bg='white', command=lambda: show("8")).place(x=90 , y=275)
Button(master=window, width=11, height=4, text='9', relief='flat', bg='white', command=lambda: show("9")).place(x=180 , y=275)
Button(master=window, width=11, height=4, text='0', relief='flat', bg='white', command=lambda: show("0")).place(x=180 , y=350)
Button(master=window, width=11, height=4, text='+', relief='flat', bg='white', command=lambda: show("+")).place(x=270 , y=275)
Button(master=window, width=11, height=4, text='-', relief='flat', bg='white', command=lambda: show("-")).place(x=270 , y=200)
Button(master=window, width=11, height=4, text='/', relief='flat', bg='white', command=lambda: show("/")).place(x=270 , y=125)
Button(master=window, width=11, height=4, text='x', relief='flat', bg='white', command=lambda: show("*")).place(x=270 , y=50)
Button(master=window, width=11, height=4, text='.', relief='flat', bg='white', command=lambda: show(".")).place(x=90 , y=350)
Button(master=window, width=11, height=4, text='=', relief='flat', bg='lightblue', command=solve).place(x=270 , y=350)
Button(master=window, width=11, height=4, text='C', relief='flat', bg='white', command=clear).place(x=0 , y=350)
Button(master=window, width=11, height=4, text='circle area', relief='flat', bg='white', command=lambda:mode()).place(x=350 , y=50)



window.mainloop()