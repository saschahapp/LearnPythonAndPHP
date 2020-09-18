"""
import math
x = eval(input("Geben Sie die Zahl ein, deren Logarithmus Sie berechnen wollen: "))
basis = eval(input("Geben Sie die Basis ein:"))
ergebnis = math.log(x,basis)
print("Der Logarithmus von", x, " zur Basis", basis, "ist", ergebnis)

# Aufgabe 1:
import random
def wuerfel ():
    ergebnis = random.randint(1, 6)
    print (ergebnis)
wuerfel()
"""
# Aufgabe 2:
import time
zeit = time.localtime()
print ("Datum: %d.%d.%d"%(zeit[2], zeit[1], zeit[0]))

    
    