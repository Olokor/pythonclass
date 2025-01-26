import tkinter as tk # this is the window builder!
from textblob import TextBlob # this is the function that corrects our spellings


window = tk.Tk() # creating window
window.title("spelling checker") # givig the window a title
window.geometry("700x400") # give the window a size
window.config(bg="#dae6f6") # give the window a backgroud color
window.resizable(False, False) # we don't want to change the size of the window while the program is running

heading = tk.Label(master=window, text="Spelling Checker", font=("arial 30 bold"), bg="#dea6f6", fg="#364971") # window heading
heading.pack(pady=10)

entry = tk.Entry(master=window, justify="center", width=30, font=("popins 25"),bg="white") # the entry
entry.pack()
entry.focus() #make the cursor bip

def correct_spelling():

    word = entry.get()
    correcter = TextBlob(word).correct()
    # result = correcter.correct()
    tk.Label(master=window, text="The Correct Spelling Is: ", font=("popins 20"), bg="#dae6f6", fg="#364971").place(x=40, y=250)
    spell.config(text=correcter)



button = tk.Button(master=window, text="Check", font=("arial 20"), bg="red",command=correct_spelling)
button.pack(pady=10)

spell = tk.Label(master=window, text="", font=("popins 20"), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)



window.mainloop()