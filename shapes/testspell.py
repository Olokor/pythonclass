import tkinter as tk
from textblob import TextBlob


window = tk.Tk()
window.title("spelling checker")
window.geometry("700x400")
window.config(bg="#dae6f6")
window.resizable(False, False)

heading = tk.Label(master=window, text="Spelling Checker", font=("arial 30 bold"), bg="#dea6f6", fg="#364971")
heading.pack(pady=10)

def correct_spelling():

    word = entry.get()
    correcter = TextBlob(word).correct()
    # result = correcter.correct()sc
    tk.Label(master=window, text="The Correct Spelling Is: ", font=("popins 20"), bg="#dae6f6", fg="#364971").place(x=40, y=250)
    spell.config(text=correcter)

entry = tk.Entry(master=window, justify="center", width=30, font=("popins 25"),bg="white")
entry.pack()
entry.focus()

button = tk.Button(master=window, text="Check", font=("arial 20"), bg="red",command=correct_spelling)
button.pack(pady=10)

spell = tk.Label(master=window, text="", font=("popins 20"), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

window.mainloop()