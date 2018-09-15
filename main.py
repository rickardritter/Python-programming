from spillebrett import Spillebrett
import time

# Hovedprogrammet spør brukeren om dimensjoner på spillebrettet og oppretter og skriver ut nulte generasjon.
# Programmet bruker en menyløkke som gjør at brukeren kan trykke enter for å kjøre programmet videre eller q
# for å avslutte programmet. Den printer også antall generasjoner og antall levende celler ved hvert steg under
# kjøring av programmet.
def main():
    x = int(input("Oppgi x dimensjonen? "))
    y = int(input("Oppgi y dimensjonen? "))
    c = Spillebrett(y,x)
    #c.tegnBrett()

    svar = input("Trykk q for avslutte programmet: ")
    while svar != "q":
        c.tegnBrett()
        print ()
        print ("Generasjon: ", c.oppdatering())
        print ("Antall levende celler: ", c.finnAntallLevende())
        #time.sleep(0.5)
        svar = input("Trykk q for avslutte programmet: ")




#starter hovedprogrammet
main()
