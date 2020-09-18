class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler
    """
    anzahl = 0
    def __init__(self, ma, mo, bj, pr):
        """
        Intialisiert ein neues Objekt Auto
        Argumente:
        * Marke (string): Marke des Gebrauchtwagens
        * Modell (string): Modell des Gebrauchtwagens
        * Baujahr (int): Baujahr des Fahrzeugs
        * Preis (int): Angestrebter Verkaufspreis
        """
        self.__Marke = ma
        self.__Modell = mo
        self.__Baujahr = bj
        self.__Preis = pr
        Auto.anzahl += 1

    
    def getMarke(self):
        return self.__Marke
    
    def getModell(self):
        return self.__Modell
    
    def getBaujahr(self):
        return self.__Baujahr

    def getPreis(self):
        return self.__Preis

    def setPreis(self, preis_neu):
        if abs(self.__Preis - preis_neu) < self.__Preis*0.05:
            self.__Preis = preis_neu
        else:
            print ("Die Abweichung zum vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis"%preis_neu + "festgelegt werden? (ja/nein) ")
            if bestaetigung == "ja":
                self.__Preis = preis_neu


class SUV(Auto):
    """
    Erstellt das Objekt SUV: abgeleitet von der Klasse Auto.
    """
    def __init__(self, ma, mo, bj, pr, allrad):
        """
        Intialisiert ein neues Objekt SUV 
        Argumente:
        * Marke (string): Marke des Gebrauchtwagens
        * Modell (string): Modell des Gebrauchtwagens
        * Baujahr (int): Baujahr des Fahrzeugs
        * Preis (int): Angestrebter Verkaufspreis
        * Allradantrieb (bool): Ist ein Allradantrieb vorhanden?
        """

        Auto.__init__(self, ma, mo, bj, pr)
        self.__Allradantrieb = allrad

    def getAllradantrieb(self):
        """
        Gibt an, ob ein Allradantrieb vorhanden ist.
        """
        return self.__Allradantrieb


#print (Auto.anzahl)
auto1 = Auto("VW", "Golf", 2011, 5000)
#print (Auto.anzahl, auto1.anzahl)
auto2 = Auto("Renault", "Clio", 2013, 6000)
#print (Auto.anzahl, auto1.anzahl, auto2.anzahl)
auto3 = Auto("Porsche", "Panamera", 2014, 25000)
#print (Auto.anzahl, auto1.anzahl, auto2.anzahl, auto3.anzahl)
#print (Auto.anzahl, auto2.anzahl, auto3.anzahl)
#wert = eval(input("Geben Sie den neuen Preis für VW Golf  ein: "))
#auto2.setPreis(wert)
#print ("Neuer Preis:", auto1.getPreis())
suv1 = SUV("Mercedes-Benz", "M-Klasse", 2014, 14000, True)
print (suv1.getAllradantrieb())
print (suv1.getMarke())









