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

fahrzeug1 = ["VW", "Golf", 2011, 5000] # Liste!
fahrzeug2 = ["BMW", "M3", 2020, 100000]
listefahrzeuge = [fahrzeug1, fahrzeug2]
fahrzeug3 = {"Marke": "VW", "Modell": "Golf", "Baujahr": 2012, "Preis": 5000}
fahrzeug3["farbe"] = "blau" # hinzufügen der Liste
print (fahrzeug3)
print (fahrzeug3["Marke"])
del fahrzeug3["Baujahr"]
print (fahrzeug3)
print (list (fahrzeug3.keys()))
print (sorted (fahrzeug3.keys()))
fahrzeug1 = dict(marke="VW", model="Golf", baujahr=2012, preis=5000) # geht nur wenn Schlüssel string ist!!
print (fahrzeug1["marke"])
fahrzeug1 = "VW", "Golf", 2011, 5000 # Tupel!
tu = "blau", # neue Tupel erstellen
fahrzeug1 = fahrzeug1 + tu # hinzufügen der neuen Tupel
print (fahrzeug1)
fahrzeug1 = "VW", "Golf", 2011, [5000]
fahrzeug1[3][0] = 4500
print (fahrzeug1)
print ("Programm für einen Buchhändler")
print ("\n")
buch1 = ["Titel", "Autor", "Artikelnummer", "Preis"]
buch2 = ["Titel2", "Autor2", "Artikelnummer2", "Preis2"]
buch3 = ["Titel3", "Autor3", "Artikelnummer3", "Preis3"]
print (buch1[0])
print (buch1[1])
print (buch1[2])
print (buch1[3])
print ("\n")
print (buch2[0])
print (buch2[1])
print (buch2[2])
print (buch2[3])
print ("\n")
print (buch3[0])
print (buch3[1])
print (buch3[2])
print (buch3[3])
print ("Programm für einen Buchhändler")
print("\n")
buch1 = {"Titel": "Titel", "Autor": "Autor", "Artikelnummer": "Artikelnummer", "Preis": "Preis"}
buch2 = {"Titel": "Titel2", "Autor": "Autor2", "Artikelnummer": "Artikelnummer2", "Preis": "Preis2"}
buch3 = {"Titel": "Titel3", "Autor": "Autor3", "Artikelnummer": "Artikelnummer3", "Preis": "Preis3"}
print (buch1["Titel"])
print (buch1["Autor"])
print (buch1["Artikelnummer"])
print (buch1["Preis"])
print ("\n")
print (buch2["Titel"])
print (buch2["Autor"])
print (buch2["Artikelnummer"])
print (buch2["Preis"])
print ("\n")
print (buch3["Titel"])
print (buch3["Autor"])
print (buch3["Artikelnummer"])
print (buch3["Preis"])
print ("Programm für einen Buchhändler")
print("\n")
buch1 = "Titel", "Autor", "Artikelnummer", "Preis"
buch2 = "Titel2", "Autor2", "Artikelnummer", "Preis2"
buch3 = "Titel3", "Autor3", "Artikelnummer3", "Preis3"
print (buch1[0])
print (buch1[1])
print (buch1[2])
print (buch1[3])
print ("\n")
print (buch2[0])
print (buch2[1])
print (buch2[2])
print (buch2[3])
print ("\n")
print (buch3[0])
print (buch3[1])
print (buch3[2])
print (buch3[3])
"""