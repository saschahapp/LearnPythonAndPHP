from tkinter import *

fenster = Tk()
fenster.geometry("300x100")
fenster.title("Python-Kurs")
rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill ="both", expand = 1)
label = Label(rahmen, text ="Willkommen zum Python-Kurs!")
label.grid(row = 1, column = 1)
button = Button(rahmen, width = 10, text = "OK", command = fenster.destroy)
button.grid(row = 2, column = 2)
class MyButton(Button):
    def aktion(self):
        print ("Sie haben den Button gedrückt")
button2 = MyButton(rahmen, width = 10, text = "Action!")
button2["command"] = button2.aktion
button2.grid(row = 2, column = 2)
fenster.mainloop()

