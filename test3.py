"""
n = 1
while n <= 100:
    print (n)
    n = n + 1

weiter = "ja"
while weiter == "ja":
    zahl = eval(input("Welche Zahl möchten Sie verdoppeln? "))
    print ("Doppelter Wert: ", zahl * 2)
    weiter = input ("Möchten Sie fortfahren? (ja/nein) ")

liste = [3, 6, 123, 54, 927]
i = 0
while i < len(liste):
    print (liste[i])
    i += 1
## alternativ mit for-schleife:
for inhalt in liste:
    print (inhalt)
# bei einer Ausgabe eines Dictionaries ist die for-schleife deutlich einfacher als eine while-schleife
dic = {"Marke": "VW", "Modell": "Golf", "Baujahr": 2011, "Preis": 5000}
for inhalt in dic:
    print (inhalt, dic[inhalt])

liste = [3, 6, 123, 54, 927]
print (liste)
for inhalt in enumerate(liste):
    liste[inhalt[0]] = inhalt[1] * 2
    print (liste)

for n in range(1, 101, 2): # zeigt nur die Geraden Zahlen von 2 - 100 an
    print (n+1)

for n in range(101, 1, -2): # zählt rückwärts
    print (n+1)

liste = [12, 18, 3, 6, 46, 234, 23]
wert = eval(input("Welcher Wert soll gesucht werden?"))
for n in liste:
    if n == wert:
        print ("Die Zahl wurde gefunden")
        break
    print (n)
    
liste = [12, 18, 3, 6, 46, 234, 23]
wert = eval(input("Welcher Wert soll gesucht werden?"))
for n in liste:
    if n == wert:
        print ("Die Zahl wurde gefunden")
        break
    print (n)
else:
    print ("Die Zahl ist nich in der Liste enthalten")

liste = [12, 18, 3, 6, 0, 46, 234, 23]
wert = eval(input("Welcher Wert soll dividiert werden?"))
for n in liste:
    if n == 0:
        print ("Fehler: Zahlen dürfen nicht durch 0 geteilt werden")
        continue
    print (wert/n)

# Aufgabe 1:
i = 1
while i <= 10:
    n = i * i
    print (n)
    i += 1

# alternativ mit for-schleife:
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in zahlen:
    quadrat = n * n
    print (quadrat)

# Aufgabe 2:
stadt = ["Berlin", "Hannover", "Passau", "Regensburg", "München", "Leipzig", "Landshut", "Ingolstadt", "Deggendorf", "Hamburg"]
# Ausgabe der Liste mit for-schleife:
for n in stadt:
    print (n)
# Ausgabe der Liste mit while-schleife:
i = 0
while i < 10:
    print (stadt[i])
    i += 1
"""
# Aufgabe 3:
i = True
while i == True:
    wert = eval(input("Geben Sie einen Wert ein, der verdoppelt werden soll:"))
    wert = wert * 2
    print ("Der doppelte Wert ist: ", wert)
    frage = input("Wollen Sie fortfahren? (ja/nein) ")
    if frage == "nein":
        i = False


