from tkinter import *
from time import strftime

window = Tk()
window.title("Digital-Clock")

label = Label(master=window, text="", font=("ds.digital 80"), bg="black", fg="cyan")
label.pack()

def time():
    global label
    string = strftime("%H:%M:%S: %p")
    label.config(text=string)
    label.after(1000, time)

time()
mainloop()