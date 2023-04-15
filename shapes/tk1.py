import tkinter as tk
from tkinter import ttk

window = tk.Tk()

def button_function():

    print("checking out the button widget in tkinter")

label1 = tk.Label(master=window, text="my first tkinter class")
label1.pack()

label2 = tk.Label(master=window, text="testing out the label in tkinter")
label2.pack()

button = ttk.Button(master=window, text="pressing button", command=button_function)
button.pack(pady='10')


tk.mainloop()