"""
n = 1
while n <= 100:
    print (n)
    n = n + 1
"""
weiter = "ja"
while weiter == "ja":
    zahl = eval(input("Welche Zahl möchten Sie verdoppeln? "))
    print ("Doppelter Wert: ", zahl * 2)
    weiter = input ("Möchten Sie fortfahren? (ja/nein) ")

