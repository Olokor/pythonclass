from tkinter import *
from tkinter import ttk, messagebox
# from textblob import TextBlob
import googletrans
from googletrans import Translator
import tkinter as tk


window = tk.Tk()
window.title("Language Translator")
window.geometry("590x390")

frame1 = Frame(master=window, height=370, width=590,relief=RIDGE, borderwidth=5, bg='#f7dc6f')
frame1.place(x=0, y=0)

Label(master=window, text="Language Translator", font=("Helvetica 20 bold"), fg='black', bg='#f7dc6f').pack(pady=10)

def treanslate():
    try:
        #     get the combo from the dictionary

        for key, value in languages.items():
            if (value == input_lang.get()):
                input_lang_key = key

#         get key of the translated combo(output)
        for key, value in languages.items():
            if (value == translate_lang.get()):
                output_lang_key = key
        words = text_entry1.get('1.0', 'end')
        translator = Translator()
        output = translator.translate(words, src=input_lang_key, dest=output_lang_key)
        text_entry2.insert('end', output.text)
    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    text_entry1.delete('1.0', 'end')
    text_entry2.delete('1.0', 'end')


languages = googletrans.LANGUAGES
lang_list = list(googletrans.LANGUAGES.values())
# print(lang_list.index('english'))
default_lang = tk.StringVar()
input_lang = ttk.Combobox(master=frame1, width=27,values=lang_list, textvariable=default_lang, state='randomly', font=("verdana 10 bold"))

input_lang.place(x=15, y=60)
input_lang.current(21)

translate_lang = tk.StringVar()
choose_lang = ttk.Combobox(master=frame1, width=27, values=lang_list, textvariable=translate_lang, state='randomly', font=('verdana 10 bold'))
choose_lang.place(x=305, y=60)
choose_lang.current(0)


text_entry1 = Text(master=frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry1.place(x=10, y=100)
text_entry2 = Text(master=frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry2.place(x=300, y=100)

btn1 = Button(master=frame1, text="Translate", command=treanslate, relief=RAISED, borderwidth=2, font=("verdana 10 bold"), bg="#248aa2", fg="white", cursor="hand2" )
btn1.place(x=185, y=300)

btn2 = Button(master=frame1, text="Clear", command=clear, relief=RAISED, borderwidth=2, font=("verdana 10 bold"), bg="#248aa2", fg="white", cursor="hand2")
btn2.place(x=300, y=300)
window.mainloop()