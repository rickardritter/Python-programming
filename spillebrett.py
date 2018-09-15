
from random import randint
from celle import Celle

# Denne klassen beskriver et todimensjonalt brett som inneholder celler.
# Spillebrettet skal holde styr på hvilke celler som skal endre status og
# oppdatere disse for hver generasjon.
# Konstruktøren tar imot dimensjoner på
# spillebrettet og lagrer disse i instansvariablene self._rader og self._kolonner.
# Rutenettet fylles med et antall Celle-objekter likt et antall rader ganger et antall
# kolonner. Self._generasjon er en instansvariabel som holder styr på generasjonsnummer og økes hver ganger
# brettet oppdateres. Konstruktøren kaller også på metoden generer, som går gjennom rutenett og sørger
# for at et tilfeldig antall celler får status "levende", som er "seed" og ugjør nulte generasjon i cellesimuleringen.
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        for e in range(rader):
            rad = []
            self._rutenett.append(rad)
            for i in range(kolonner):
                rad.append(Celle())
        self._generasjon = 0
        self.generer()


        #print(self._rutenett)
# Denne metoden bruker en nøstet for-løkke for å skrive ut hvert element i rutenett.
# For å unngå linjeskifte etter hver utskrift, avsluttes utskriften med en tom streng, print(tegn, end="").

    def tegnBrett(self):
        for e in range(self._rader):
            for i in range(self._kolonner):
                tegn = self._rutenett[e][i].hentStatusTegn()
                print(tegn, end="")
            print()
        print()

# Denne metoden inneholder to lister, døde celler og levende celler. Hvor deres status byttes om på.
# Metoden går igjennom rutenett ved hjelp av en nøstet løkke. For hver celle skal den sjekke om cellen er død
# eller levende. Deretter beregne om den skal endre status på bakgrunn av antall levende naboer.
# Her blir alle naboene til en celle og teller antallet som lever. Celler som endrer status skal legges
# inn i den riktige av de to listene.
# Når alle cellene er sjekket og listene er fylt med Celle-objekter skjer selve oppdateringen.
    def oppdatering(self):
        celler_doed = []
        celler_levende = []

        for x in range(self._rader):
            for y in range(self._kolonner):
                nabo = self.finnNabo(y, x)
                levende_naboer = []
                for celle in nabo:
                    #print("levende?", celle.erLevende())
                    if celle.erLevende():
                        levende_naboer.append(celle)
                if self._rutenett[x][y].erLevende():
                    #print("celle",x,y,"hadde", len(levende_naboer), "naboer")
                    if len(levende_naboer) == 2 or len(levende_naboer) ==3:
                        celler_levende.append(self._rutenett[x][y])
                    else:
                        celler_doed.append(self._rutenett[x][y])
                else:
                    if len(levende_naboer) == 3:
                        celler_levende.append(self._rutenett[x][y])
                    else:
                        celler_doed.append(self._rutenett[x][y])

        for levende in celler_levende:
            levende.settLevende()
        for doed in celler_doed:
            doed.settDoed()

        self._generasjon +=1
        return self._generasjon

# Metoden beregner og ruternere antall levende celler. Dette gjøres ved å gå igjennom
# rutenett og øke en teller for hver levende celle.
    def finnAntallLevende(self):
        antallLevendeceller = 0
        for e in range(self._rader):
            for d in range(self._kolonner):
                if self._rutenett[e][d].erLevende():
                    antallLevendeceller += 1
        return antallLevendeceller

# Denne meotden genererer et tilfeldig tall for hver celle (her mellom 0 og 3) og sammenlikner
# det med et statisk sjekketall(her 3). Dersom tallene mathcer vil cellene settes til "levende".
    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0,3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()

# Metoden går igjennom de ni muulige plassene rundt en celle, men luker ut senteret(som er selve cellen og ikke naboen)
# Samt plasseringen som er for små eller for store til å eksistere i spillebrettet(utenfor kanten av brettet).
# Alle gyldige naboer legges i en liste av naboer som returneres.
    def finnNabo(self,x,y):
        naboliste = []
        for i in range(-1,2):
            for j in range(-1,2):
                naboX = x+i
                naboY = y+j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self._kolonner-1 or naboY > self._rader-1) != True:
                        naboliste.append(self._rutenett[naboY][naboX])
        return naboliste


"""
s = Spillebrett(3,5)
s.tegnBrett()
s.oppdatering()
s.tegnBrett()
"""
