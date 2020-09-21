try:
    x = eval(input("Wert:" ))
    print ("Ergebnis:", 4/x)
except ZeroDivisionError:
        print ("Es ist nicht möglich, einen Wert durch 0 zu teilen!")
        print ("Auf Wiedersehen")

