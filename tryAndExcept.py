import sys
"""
try:
    x = eval(input("Wert:" ))
    print ("Ergebnis:", 4/x)
except ZeroDivisionError:
        print ("Es ist nicht möglich, einen Wert durch 0 zu teilen!")
print ("Auf Wiedersehen")


# Alternativ mit 2 unterschiedlichen Ausnahmen:

try:
    x = int(input("Wert:" ))
    print ("Ergebnis:", 4/x)
except (ZeroDivisionError, ValueError):
        print ("Es ist ein Fehler aufgetreten")
print ("Auf Wiedersehen")

# Für jeden Fehlertyp einen eigenen Except Block erstellen:

try:
    x = int(input("Wert: "))
    print ("Ergebnis:", 4/x)
except ZeroDivisionError:
    print ("Es ist nicht möglich durch 0 zu teilen")
except ValueError:
    print ("Sie müssen eine ganze Zahl eingeben!")
except:
    print ("Folgender Fehler ist aufgetreten:", sys.exc_info()[0])
else:
    print ("Das Ergebnis wurde erfolgreich berechnet")
print ("Auf Wiedersehen")

# Programm, dass den Schlüsselbegriff finally nutz:

class Obj:
    wert = 4
    
try:
    objekt = Obj()
    x = int(input("Wert: "))
    print ("Ergebnis:", Obj.wert/x)
except ZeroDivisionError:
    print ("Es ist nicht möglich durch 0 zu teilen!")
else:
    print ("Das Ergebnis wurde erfolgreich berechnet")
finally:
    del objekt
    print ("Objekt zerstört!")
print ("Auf Wiedersehen!")

# Programm mit selbstdefinierter Ausnahme:

class OutOfRangeError(Exception):
    def __init__(self, wert):
        self.Wert = wert

try:
    x = int(input("Geben Sie einen Wert zwischen 10 und 20 ein: "))
    if x > 20 or x < 10:
        raise OutOfRangeError (x)
    print ("Ergebnis:", 4/x)
except OutOfRangeError as fehler:
    print ("Die Zahl", fehler.Wert, "liegt nicht zwischen 10 und 20")
except ValueError:
    print ("Sie müssen eine ganze Zahl eingeben!")
print ("Auf Wiedersehen!")


# Aufgabe1: 

import sys

try:
    x = eval(input("Geben Sie den zu dividierenden Wert ein: "))
    y = eval(input("Geben Sie den Wert ein, durch den Wert1 geteilt werden sollte: "))
    print ("Ergebnis:", x/y )
except ZeroDivisionError:
    print ("Wert 2 darf nicht 0 sein, da durch 0 nicht geteilt werden kann!")
except TypeError:
    print ("Es muss eine Zahl eingegeben werden!")
except:
    print ("Der Fehler ist: ", sys.exc_info()[0])
"""

# Aufgabe 2:

class OddError(Exception):
    def __init__(self, wert):
        self.Wert = wert

try:
    wort = input("Geben Sie ein Wort mit einer geraden"+ "Anzahl an Buchstaben ein: ")
    if len(wort)%2 == 1:
        raise OddError(wort)
    mitte = int(len(wort)/2)
    teil1 = wort[:mitte]
    teil2 = wort[mitte:]
    print ("Erste Hälfte:", teil1)
    print ("Zweite Hälfte", teil2)
except OddError as fehler:
    print ('Das Wort "'+wort+'" hat eine ungerade Anzahl an Buchstaben')
print ("Auf Wiedersehen!")







    