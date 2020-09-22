"""
from tkinter import *

class MyButton(Button):
    def addieren (self):
        zahl1 = int(eingabe1.get())
        zahl2 = int(eingabe2.get())
        eingabe1.delete(0, 'end')
        eingabe2.delete(0, 'end')
        ausgabe.delete(0, 'end')
        ausgabe.insert(0, zahl1 + zahl2)

fenster = Tk()
fenster.geometry("300x300")
fenster.title("Rechner")
rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)
rahmen.pack(fill = "both", expand = 1)
label1 = Label(rahmen, text = "Zahl1: ")
label1.place(x = 20, y = 30)
label2 = Label(rahmen, text = "Zahl2: ")
label2.place(x = 170, y = 30)
eingabe1 = Entry(rahmen, bd = 2, width = 10)
eingabe1.place(x = 20, y = 70)
eingabe2 = Entry(rahmen, bd = 2, width = 10)
eingabe2.place(x = 180, y = 70)
button = MyButton(rahmen, text = "Addieren")
button["command"] = button.addieren
button.place( x = 100, y = 120)
label3 = Label(rahmen, text = "Ergebnis: ")
label3.place(x = 50, y = 180)
ausgabe = Entry(rahmen, bd = 2, width = 10)
ausgabe.place( x = 120, y = 180)
fenster.mainloop()
"""

# Aufgabe 2:

from tkinter import *

class MyButton(Button):
    def aktion (self):
        if var.get() == 1:
            fenster2 = Tk()
            fenster2.geometry("200x100")
            fenster2.title("Hinweis")
            label = Label(fenster2, text = "Checkbox ist ausgewählt!")
            label.pack(fill="both", expand=1)
    def aktion2 (self):
        print (var.get())
        
fenster = Tk()
fenster.geometry("300x300")
fenster.title("Python-Kurs")
rahmen = Frame(fenster, relief="ridge", borderwidth = 5)
rahmen.pack(fill="both", expand = 1)
var = IntVar()
checkbutton = Checkbutton(rahmen, text = "Bestätigen", variable = var)
button = MyButton(rahmen, text = "Eingabe")
button["command"] = button.aktion
button.pack()
fenster.mainloop()







