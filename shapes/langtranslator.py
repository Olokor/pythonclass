import tkinter as tk
from tkinter import ttk
import googletrans
from googletrans import Translator

window = tk.Tk()
window.title("Language Translator")
window.geometry("590x390")
window.resizable(False, False)

frame1 = tk.Frame(master=window, height=370, width=590, relief="ridge", borderwidth=5, bg="#f7dc67")
frame1.place(x=0, y=0)

heading = tk.Label(master=window, text="Language Translator", font=("Helvetica 20 bold"), fg="black", background="#f7dc67")
heading.pack(pady=10)

def clear():
    entry1.delete("1.0", "end")
    entry2.delete("1.0", "end")

def translate():
    for key, value in lang.items():
        if value == default_lang.get():
            input_lang_key = key
    
    for key, value in lang.items():
        if value == translate_lang.get():
            output_lang_key = key
    
    words = entry1.get("1.0", "end")
    googletranslator = Translator()
    output = googletranslator.translate(words, src=input_lang_key, dest=output_lang_key)
    entry2.insert("end", output.text)


lang = googletrans.LANGUAGES
display_lang = list(lang.values())
default_lang = tk.StringVar()
user_language = ttk.Combobox(master=window, width=27, values=display_lang, textvariable=default_lang, font=("verdana 10 bold"))
user_language.place(x=15, y=60)
user_language.current(21)

translate_lang = tk.StringVar()
choose_lang = ttk.Combobox(master=window, width=27, values=display_lang, textvariable=translate_lang, font=("verdana 10 bold") )
choose_lang.place(x=305, y=60)
choose_lang.current(0)

entry1 = tk.Text(master=frame1, width=31, height=10, borderwidth=5, relief="ridge", font=("verdana 10") )
entry1.place(x=10, y=100)

entry2 = tk.Text(master=frame1, width=31, height=10, borderwidth=5, relief="ridge", font=("verdana 10"))
entry2.place(x=300, y=100)

btn1 = tk.Button(master=frame1, text="Translate", relief="ridge", borderwidth=2, font=("verdana 10"), bg="#248aa2", fg="white", cursor="hand2", command=translate)
btn1.place(x=195, y=300)

btn2 = tk.Button(master=frame1, text="Clear", relief="ridge", borderwidth=2, font=("verdana 10"), bg="#248aa2", fg="white", cursor="hand2", command=clear)
btn2.place(x=300, y=300)





window.mainloop()