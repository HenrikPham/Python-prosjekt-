#Lager en en klasse som representerer et elevsystem 
class Elevsystem: 

    #Lager en oversikt av elevers navn, elevID, karakterer og klasse
    def __init__(self, skole, navn, elevID, karakterer, klasse):
        self.skole = skole
        self.navn = navn
        self.elevID = elevID
        self.karakterer = karakterer
        self.klasse = klasse

    #Lager en funksjon for å vise informasjon om en elev
    def vis_informasjon(self, elev): #Viser informasjon om en elev
        print("\nInformasjon om elev:")
        print(f"Skole: {self.skole.navn}")
        print(f"Navn: {elev.navn}")
        print(f"ElevID: {elev.elevID}")
        print(f"Karakterer: {elev.karakterer}")
        print(f"Klasse: {elev.klasse}")

#Lager en klasse for å representere en elev
class Elev: 
    def __init__(self, navn, elevID, karakterer, klasse): #Konstruktør for klassen Elev som tar inn navn, elevID, karakterer og klasse som argumenter
        self.navn = navn #Setter navnet på eleven
        self.elevID = elevID #Setter elevID til eleven
        self.karakterer = karakterer #Setter karakterene til eleven
        self.klasse = klasse #Setter klassen til eleven

#Lager en klasse Skole som respresenterer en skole lagrer flere elever og håndtere funksjonene under 
class Skole:

    def __init__(self, navn): #Lager en oversikt av skolens navn og en liste over elever
        self.navn = navn
        self.elever = []

    def vis_elever(self): #Viser en liste over elever i skolen
        print(f"Elever i {self.navn}:") 
        for elev in self.elever:
            print(f"  {elev.navn} (ID: {elev.elevID}, Klasse: {elev.klasse})")
    
    def legg_til_elev(self, elev): #Legger til en elev i skolen
        self.elever.append(elev)

    def fag_info(self, elev): #Viser faginformasjon for en elev
        print(f"Faginformasjon for {elev.navn}:")
        for fag, karakter in elev.karakterer.items():
            print(fag, karakter)

    def legg_til_karakterer(self, elev, fag, karakterer_liste):
        try:
            if isinstance(karakterer_liste, str):
                karakterer_liste = [int(k.strip()) for k in karakterer_liste.split(",") if k.strip()]

            # Sørg for at karakterer er en dictionary
            if not isinstance(elev.karakterer, dict):
                elev.karakterer = {}

            # Hvis faget ikke finnes fra før → opprett liste
            if fag not in elev.karakterer:
                elev.karakterer[fag] = []

            # Legg til flere karakterer
            elev.karakterer[fag].extend(karakterer_liste)
            print(f"Karakterer lagt til i {fag}: {karakterer_liste}")
        except ValueError:
            print("Feil input! Skriv tall med komma, f.eks: 5,4,3")

    def get_elever(self): #Henter listen over elever i skolen
        return self.elever

    def regn_ut_gjennomsnitt(self, elev):
        alle_karakterer = []
        for liste in elev.karakterer.values():
            alle_karakterer.extend(liste)
        karakterer_input = input("Skriv karakterer (med komma): ")

        try:
            karakterer_liste = [int(k.strip()) for k in karakterer_input.split(",")]
        except ValueError:
            print("Du må skrive tall separert med komma!")
            return
        
        if len(alle_karakterer) == 0:
            return 0
        
        return sum(alle_karakterer) / len(alle_karakterer)

    #Lager funksjoner for å hente informasjon om elevenes navn, elevID, karakterer og klasse
    def get_navn(self): #Henter navnet til eleven
        return self.navn
    
    def get_elevID(self): #Henter elevID til eleven
        return self.elevID
    
    def get_elever(self): #Henter listen over elever i skolen
        return self.elever

    def get_karakterer(self): #Henter karakterene til eleven
        return self.karakterer
    
    def get_klasse(self): #Henter klassen til eleven
        return self.klasse
    
    #Lager funksjoner for å sette informasjon om elevenes navn, elevID, karakterer og klasse
    def set_navn(self, navn): #Setter navnet til eleven
        self.navn = navn

    def set_elevID(self, elevID): #Setter elevID til eleven
        self.elevID = elevID

    def set_elever(self, elever): #Setter listen over elever i skolen
        self.elever = elever

    def set_karakterer(self, karakterer): #Setter karakterene til eleven
        self.karakterer = karakterer

    def set_klasse(self, klasse): #Setter klassen til eleven 
        self.klasse = klasse

    #Lager funksjonen for å vise informasjon om en elev
    def vis_informasjon(self, elev): #Viser informasjon om en elev
        print("\nInformasjon om elev:")
        print(f"Skole: {self.skole.navn}")
        print(f"Navn: {elev.navn}")
        print(f"ElevID: {elev.elevID}")
        print(f"Karakterer: {elev.karakterer}")
        print(f"Klasse: {elev.klasse}") 

#Lager en hovedprogram som kjører elevsystemet og skolen
def main():
    #Lager en skole
    skole = Skole("Kongsvinger Videregående Skole")

    #Lager elever
    elev1 = Elevsystem("Navn1", "12345", [5, 4, 3], "10A")
    elev2 = Elevsystem("Navn2", "67890", [4, 4, 4], "10B")

    #Legger til elever i skolen
    skole.legg_til_elev(elev1)
    skole.legg_til_elev(elev2)

    #Viser informasjon om elevene
    skole.vis_informasjon(elev1)
    skole.vis_informasjon(elev2)

if __name__ == "__main__":
    skole = Skole("Kongsvinger Videregående Skole")
    
    while True:
        print("\nVelkommen til elevsystemet!")
        print("1. Legg til elev")
        print("2. Vis elever")
        print("3. Legg til karakter for elev")
        print("4. Vis gjennomsnittskarakter for elev")
        print("5. Avslutt")

        valg = input("Velg et alternativ: ")

        if valg == "1":
            navn = input("Skriv inn elevens navn: ")
            elevID = input("Skriv inn elevens ID: ")
            klasse = input("Skriv inn elevens klasse: ")
            elev = Elevsystem(skole, navn, elevID, [], klasse)
            skole.legg_til_elev(elev)
            print(f"Elev {navn} lagt til i skolen.")
        elif valg == "2":
            elever = skole.get_elever()
            if not elever:
                print("Ingen elever i skolen.")
            else: 
                print("\nElever i skolen:")
                for elev in skole.get_elever():
                    print(f"Skole: {elev.skole.navn}, Navn: {elev.navn}, ID: {elev.elevID}, Klasse: {elev.klasse}, fag med karakterer: {elev.karakterer}")
        elif valg == "3":
            elevID = input("Skriv inn elevens ID: ")
            fag = input("Skriv inn faget: ")
            karakterer_input = input("Skriv karakterer (med komma): ")
            karakterer_liste = [int(k.strip()) for k in karakterer_input.split(",")]
            
            elev = next((e for e in skole.get_elever() if e.elevID == elevID), None)
            
            if elev:
                skole.legg_til_karakterer(elev, fag, karakterer_liste)
            else:
                print("Elev ikke funnet.")
        elif valg == "4":
            elevID = input("Skriv inn elevens ID: ")
           
            elev = next((e for e in skole.get_elever() if e.elevID == elevID), None)
            
            if elev:
                gjennomsnitt = skole.regn_ut_gjennomsnitt(elev)
                print(f"Gjennomsnittskarakter for {elev.navn}: {gjennomsnitt}")
            else:
                print("Elev ikke funnet.")
        elif valg == "5":
            print("Avslutter elevsystemet. Ha en fin dag!")
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")