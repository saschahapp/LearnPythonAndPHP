"""
def begruessung ():
    print ("Herzlich Willkommen")
begruessung()

def begruessung (name):
    print ("Herlich Willkommen,", name)
begruessung("Peter")
begruessung("Max")

def begruessung (name):
    print ("Herzlich Willkommen,", name)
eingabe = input("Geben Sie bitte Ihren Namen ein:")
begruessung(eingabe)

def begruessung (name, zahl):
    print ("Herzlich Willkommen,", name)
    print ("Die eingegebene Zahl lautet:",zahl)
eingabe1 = input("Geben Sie ihren Namen ein: ")
eingabe2 = eval(input("Geben Sie eine Zahl ein: "))
begruessung (eingabe1, eingabe2)

def personendaten (name = "unbekannt", wohnort = "unbekannt", alter = "unbekannt"):
    print ("Name:", name)
    print ("Wohnort:", wohnort)
    print ("Alter:", alter)
personendaten ()
personendaten ("Herbert Müller")
personendaten ("Herbert Müller", "Frankfurt")
personendaten ("Herbert Müller", "Frankfurt", 57)
personendaten (wohnort = "Frankfurt")

def formel (x):
    wert = 2 * x * x + 4 * x + 9
    return wert
ergebnis = formel(4)
print (ergebnis)

# alternativ:
def formel (x):
    return 2 * x * x + 4 * x + 9
print (formel(4))

def formel (x):
    wert1 = 2 * x * x + 4 * x + 9
    wert2 = 3 * x * x + 2 * x - 7
    return [wert1, wert2]
ergebnisse = formel (4)
print ("Ergebnis der ersten Formel:", ergebnisse[0])
print ("Ergebnis der zweiten Formel:", ergebnisse[1])

def formel (x):
    if 2 * x * x + 4 * x + 9 < 50:
        return 2 * x * x + 4 * x + 9
    else:
        return 3 * x * x + 2 * x - 7
eingabe = eval(input("Geben Sie eine Zahl ein:"))
print (formel(eingabe))

import modul_bsp
eingabe = eval(input("Geben Sie eiene Zahl ein: "))
print (modul_bsp.formel(eingabe))

# Aufgabe 1:
def abfrageAusgabeZweierschritten (zahl1, zahl2):
    if zahl1 > zahl2 :
        for n in range (zahl2, zahl1, 2):
            print (n)
    elif zahl1 < zahl2 :
        for n in range (zahl1, zahl2, 2):
            print (n)
eingabe1 = eval(input("Geben Sie die erste Zahl ein:"))
eingabe2 = eval(input("Geben Sie die zweite Zahl ein:"))
abfrageAusgabeZweierschritten(eingabe1, eingabe2)
"""
# Aufgabe 2:
def nutzernamenPasswortKombination (nutzernamen, passwort):
    user1 = ["maxihuber", "5TG36"]
    user2 = ["petermil", "3ER32"]
    user3 = ["master", "TP490"]
    eingabe = [nutzernamen, passwort]
    if eingabe == user1 or eingabe == user2 or eingabe == user3:
        print ("Anmeldung erfolgreich!")
    else:
        print ("Anmeldung fehlgeschlagen! Nutzernamen oder Passwort überprüfen!")
eingabe1 = input ("Bitte geben Sie Ihren Nutzernamen ein: ")
eingabe2 = input ("Bitte geben Sie Ihr Passwort ein: ")
nutzernamenPasswortKombination (eingabe1, eingabe2)


