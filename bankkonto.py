#Lager en enkel klasse som representerer et bankkonto
class BankKonto:

    #Lager en startsaldo for kontoen når den opprettes, standard er 1000
    def __init__(self, start_saldo=1000):
        self.saldo = start_saldo

    #Metode for å vise menyen for brukeren
    def vis_meny(self):
        print("\nVelkommen til BankKonto!")
        print("1. Sjekk saldo")
        print("2. Sett inn penger")
        print("3. Ta ut penger")
        print("4. Avslutt konto")

    #Metode for å sjekke saldoen på kontoen
    def sjekk_saldo(self):
        print(f"Din nåværende saldo er: {self.saldo} kr")

    #Metode for å sette inn penger på kontoen
    def sett_inn(self, beløp):
        if beløp > 0:
            self.saldo += beløp
            print(f"Du har satt inn {beløp} kr. Ny saldo: {self.saldo} kr")
        else:
            print("Beløpet må være positivt.")
    
    #Metode for å ta ut penger fra kontoen
    def ta_ut(self, beløp):
        if beløp > 0:
            if beløp <= self.saldo:
                self.saldo -= beløp
                print(f"Du har tatt ut {beløp} kr. Ny saldo: {self.saldo} kr")
            else:
                print("Du har ikke nok penger på kontoen.")
        else:
            print("Beløpet må være positivt.")
    
#Hovedprogrammet som kjører bankkontoen
if __name__ == "__main__":
    konto = BankKonto()
    
    while True:
        konto.vis_meny()
        valg = input("Velg et alternativ (1-4): ")
        
        if valg == '1':
            konto.sjekk_saldo()
        elif valg == '2':
            try:
                beløp = float(input("Skriv inn beløpet du vil sette inn: "))
                konto.sett_inn(beløp)
            except:
                print("Du må skrive inn et gyldig beløp.")
        elif valg == '3':
            beløp = float(input("Skriv inn beløpet du vil ta ut: "))
            konto.ta_ut(beløp)
        elif valg == '4':
            print("Takk for at du brukte BankKonto. Ha en fin dag!")
            break

    # Avslutter programmet når brukeren velger å avslutte kontoen
    def avslutt_konto(self):
        print("Kontoen er nå avsluttet.")
        self.saldo = 0