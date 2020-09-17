"""
a = eval(input("Bitte geben Sie die Zahl 5 ein:"))
if a == 5:
    print ("Die Eingabe ist richtig")
a = input('Geben Sie bitte das Wort "Hallo" ein:')
if a == "Hallo":
    print ("Die Eingabe war richtig")
else:
    print ("Die Eingabe war falsch")
a = eval(input("Geben Sie bitte die Zahl 5 ein:"))
b = eval(input("Geben Sie jetzt bitte die Zahl 10 ein:"))
if a == 5 and b == 10:
    print ("Die Eingabe ist richtig")
if a != 5 and b == 10:
    print ("Antwort A ist falsch, B ist richtig")
if a == 5 and b != 10:
    print ("Antwort A ist richtig, B ist falsch")
if a != 5 and b != 10: # alternativ:  if not (a == 5 and b == 10):
    print ("Beide Antworten sind falsch")
print ("Gebrauchtwagenbörse")
fahrzeuge = [{"Marke": "BMW", "Modell": "M3", "Motor": "340kW", "Preis": 80000}, {"Marke": "BMW", "Modell": "M2", "Motor": "290kW", "Preis": 59000},
{"Marke": "BMW", "Modell": "M8", "Motor": "460kW", "Preis": 204000}]
maximalpreis = eval(input("Bitte geben Sie den Höchstbetrag in Euro ein:"))
if maximalpreis >= 204000:
    print (fahrzeuge[:])
elif  maximalpreis >= 80000:
    print (fahrzeuge[:2])
elif maximalpreis >= 59000:
    print (fahrzeuge[1])
else:
    print ("Wir haben leider kein Fahrzeug in dieser Preiskategorie!")
# Aufgabe 2:
richtig = 0
rechnung1 = eval(input("5 + 13 ="))
if rechnung1 == 18:
    richtig = richtig + 1 # or richtig += 1
rechnung2 = eval(input("15 + 12 ="))
if rechnung2 == 27:
    richtig = richtig + 1 # or richtig += 1
rechnung3 = eval(input("12 - 3 ="))
if rechnung3 == 9:
    richtig = richtig + 1 # or richtig += 1
rechnung4 = eval(input("12 * 4 ="))
if rechnung4 == 48:
    richtig = richtig + 1 # or richtig += 1
rechnung5 = eval(input("25 / 5 ="))
if rechnung5 == 5:
    richtig = richtig + 1 # or richtig += 1
if richtig == 5:
    print ("Super! Alle Aufgaben richtig gelöst!")
elif richtig >= 3:
    print ("Gute Leistung!")
elif richtig >= 1:
    print ("Viele Fehler: weitere Übung erfoderlich!")
else:
    print ("Dringend Nachhilfe benötigt!")
"""



