import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

window = ttk.Window(themename="darkly")
window.geometry('350x150')

window.title('demo')
title_label = tk.Label(master=window, text='Hours to seconds', font='calibri 24 bold')
title_label.pack()

# button function
def convert():
    get_input = entry.get()
    km_output = int(get_input) * 3600
    output_string.set(km_output)

# input fields
input_frame = ttk.Frame(master=window)
entryint = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryint)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='output', font='calibri 24', textvariable=output_string)
output_label.pack()

tk.mainloop()
