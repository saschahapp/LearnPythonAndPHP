class Wohnung:
    """
    Erfasst eine Ferienwohung im Objekt Wohnung.
    """
    def __init__(self, name, ort, betten, preis):
        """
        Intialisierung des Objekts Wohnung.
        Argumente:
        * Name (string): Name der Ferienwohung
        * Ort (string): Standort der Ferienwohung
        * Betten (int): Anzahl der Betten in der Ferienwohung
        * Preis (int): Preis pro Übernachtung
        """
        self.__Name = name
        self.__Ort = ort
        self.__Betten = betten
        self.__Preis = preis

    def getName(self):
        """
        Gibt den Namen der Ferienwohung zurück
        """
        return self.__Name

    def getOrt(self):
        """
        Gibt den Ort der Ferienwohung zurück
        """
        return self.__Ort

    def getBetten(self):
        """
        Gibt die Anzahl der Betten zurück
        """
        return self.__Betten

    def getPreis(self):
        """
        Gibt den Preis für eine Übernachtung zurück
        """
        return self.__Preis

    def setPreis(self, preis_neu):
        """
        Legt einen neuen Preis fest
        """
        self.__Preis = preis_neu

# Hauptprogramm

wohnung1 = Wohnung("Meerblick", "Sylt", 4, 69)
wohnung2 = Wohnung("Alpen-Panorama", "Füssen", 5, 74)
wohnung3 = Wohnung("Am Seeufer", "Konstanz", 3, 58)

print ("Wohnung 1:", wohnung1.getName(), wohnung1.getOrt(), wohnung1.getBetten(), wohnung1.getPreis())
print ("Wohnung 2:", wohnung2.getName(), wohnung2.getOrt(), wohnung2.getBetten(), wohnung2.getPreis())
print ("Wohnung 3:", wohnung3.getName(), wohnung3.getOrt(), wohnung3.getBetten(), wohnung3.getPreis())