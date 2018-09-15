# Kort forklart skal programmet holde styr om en celle er levende eller død. Simuleringen utspiller seg
# over mange generasjoner, der celler dør eller lever i en generasjon avhengig av sine omgivelser.

# Klassen nedenfor beskriver en celle i simuleringen. En celle skal ha en variabel som beskriver
# status til cellen til henholdsvis "død" og "levende".

class Celle:
    # Konstruktør for klassen som oppretter cellen med status "død" som utgangspunkt.
    # Her kaller jeg på metoden settDoed i konstruktøren. Det finnes andre metoder, men fant ut at denne teknikken
    # funkerte som en snarvei i kodingen.
    def __init__(self):
        self.settDoed()

    # Endre status til cellen ved bruk av bolsk algebra
    def settDoed(self):
        self._levende = False
    # Endre status til cellen ved bruk av bolsk algebra
    def settLevende(self):
        self._levende = True

    # Henter status. Med andre ord returnerer den statusen til cellen, True hvis cellen er levende og False ellers.
    # Dette har jeg løst ved ruternere instansvariabelen self._levende
    def erLevende(self):
        return self._levende
    # Metoden returnerer en tegnepresentasjon av cellens status til bruk i tegningen av brettet.
    # Dersom cellen er "levende" skal det returneres en "O", mens hvis den er død returneres et punktum.
    def hentStatusTegn(self):
        if self._levende == True:
            return "O"
        else:
            return "."
    # Returner en streng som inneholder en utskrivbar representasjon av et objekt.
    # Dette er en metode som ikke er nødvendig, men er en liten lifehack.
    def __repr__(self):
        return self.hentStatusTegn()
