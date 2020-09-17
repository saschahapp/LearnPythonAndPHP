"""
print ("Gebrauchtwagen-Programm")
print ("Herzlich Willkommen")
print ("In diesem Programm sind diverse Funktion möglich")
# Funktionen hinzufügen
print (5 + 2)
print ("5 + 2")
# variable_1 = 5  erlaubt
#_1_varibale = 5  erlaubt
#1_Variable = 5   nicht erlaubt !
a = 5
print ("Wert der Variablen a:",a)
print ("Geben Sie einen Wert ein:")
inhalt = eval(input())
inhalt = inhalt*2
print ("Doppleter Wert: ", inhalt)
# alternativ:
inhalt = eval(input("Geben Sie bitte eine Zahl ein:"))
inhalt = inhalt*2
print ("Der doppelte Wert ist : ", inhalt) 
# alternativ ohne eval funktion:
inhalt = input("Geben Sie eine Zahl ein:")
inhalt = float(inhalt)*2
print ("Doppelter Wert: ", inhalt) 
text = "hallo"
print ("Wert vorher:",text)
text = text.upper()
print ("Wert nacherher:",text)
a = 3.5
print ( type(a))
a = True
print ( type(a))
wert1 = input("Geben Sie den ersten Wert ein:")
wert2 = input("Geben Sie den zweiten Wertt ein:")
wert3 = int(wert1) + int(wert2)
print ("Erster + zweiter Wert ist:",wert3)
inhalt = eval(input("Geben Sie einen beliegen Wet ein:"))
print ("Datentyp des Wertes:", type(inhalt))
"""
fahrzeug1 = ["VW", "Golf", 2011, 5000]
fahrzeug2 = ["BMW", "M3", 2020, 100000]
listefahrzeuge = [fahrzeug1, fahrzeug2]
fahrzeug3 = {"Marke": "VW", "Modell": "Golf", "Baujahr": 2012, "Preis": 5000}
print (fahrzeug3)
print (fahrzeug3["Marke"])
del fahrzeug3["Baujahr"]
print (fahrzeug3)
print (list (fahrzeug3.keys()))
print (sorted (fahrzeug3.keys()))
fahrzeug1 = dict(marke="VW", model="Golf", baujahr=2012, preis=5000) # geht nur wenn Schlüssel string ist!!
print (fahrzeug1["marke"])
