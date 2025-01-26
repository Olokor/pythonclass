from tkinter import *


window =  Tk()

entry_output = StringVar()
entry = Entry(window, textvariable=entry_output)
entry_str = ""
entry.pack(padx=20, pady=20)

def show(letter):
    global entry_str
    entry_str += str(letter)
    entry_output.set(entry_str)



Button(window, text="A", command=lambda:show("A")).pack()

Button(window, text="B", command=lambda:show("B")).pack()

window.mainloop()