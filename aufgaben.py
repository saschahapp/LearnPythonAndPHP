# Aufgabe 1:

f = open('gaeste.txt', 'a')
i = True
while i == True:
    namen = input("Geben Sie einen Namen ein: ")
    f.write(namen+"\n")
    fortsetzen = input("Wollen Sie einen weiteren Namen hinzufügen? (ja/nein) ")
    if fortsetzen != "ja":
        i = False

# Aufgabe 2:

f = open('gaeste.txt', 'r')
liste = f.readlines()
f.close()
geloescht = False
eingabe = input("Welchen Gast möchten Sie löschen")
for i in range(len(liste)):
    if liste[i] == eingabe+"\n":
        f = open('gaeste.txt', 'w')
        liste = liste[i] + liste[i+1:]
        for linie in liste:
            f.write(linie)
            print (eingabe, "wurde erfolgreich gelöscht.")
            geloescht = True
            break
        if not geloescht:
            print(eingabe, "ist nicht in der Liste enthalten.")