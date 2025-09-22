import datetime # håndtering av dato og tid
import os # håndtering av operativsystem
import json # håndtering av JSON data


file_path = "data.json" # vei til datafilen

# data storage 
library_data = {"books": [ # liste over bøker i biblioteket
    # tittel, forfatter, tilgjengelighet
    {"title": "1984", "author": "George Orwell", "availability": True }, # true = tilgjengelig, false = utlånt
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "availability": False }, # utlånt
    {"title": "The Great Gatsby", "author": "F, Scott Fitzgerald", "availability": True }, # tilgjengelig
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "availability": True }, # tilgjengelig
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "availability": False }, # utlånt
    {"title": "Pride and Prejudice", "author": "Jane Austen", "availability": True }, # tilgjengelig
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "availability": True }, # tilgjengelig
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "availability": False }, # utlånt
    {"title": "Animal Farm", "author": "George Orwell", "availability": True }, # tilgjengelig
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "availability": True }, # tilgjengelig
    {"title": "Cat Warriors", "author": "Erin Hunter", "availability": True }  # tilgjengelig
]} 

def save_library_data(file_path, library_date): # funksjon for å lagre bibliotekdata til en JSON-fil
    with open(file_path, 'w', encoding='utf-8') as f: # åpne fil i skrive-modus
        json.dump(library_data, f, indent=2) # lagre data til fil med innrykk på 2 mellomrom

def load_library_data(file_path): # funksjon for å laste bibliotekdata fra en JSON-fil
    with open(file_path, 'r', encoding='utf-8') as f: # åpne fil i lese-modus
        return json.load(f) # returnere data fra fil

# Bilbliotekshjememeside
def library_homepage(): # funksjon for å vise hovedmenyen
    print("Velkommen til Biblioteket!") # velkomstmelding
    print("1. Vis alle bøker") # menyvalg 1 - vis alle bøker
    print("2. Søk etter en bok") # menyvalg 2 - søk etter en bok
    print("3. Lån en bok") # menyvalg 3 - lån en bok    
    print("4. Returner en bok") # menyvalg 4 - returner en bok
    print("5. Avslutt") # menyvalg 5 - avslutt programmet

# Klasse for bibliotek
class Library: # klasse for bibliotek
    def __init__(self, file_path): # initialiseringsmetode
        self.file_path = file_path # lagre filsti
        if os.path.exists(file_path): # sjekke om filen eksisterer
            self.data = load_library_data(file_path) # laste data fra fil
        else:
            self.data = library_data # bruke standard data
            save_library_data(file_path, self.data) # lagre standard data til fil

    def show_all_books(self): # metode for å vise alle bøker
        print("\nAlle bøker i biblioteket:") # overskrift
        for book in self.data["books"]: # iterere gjennom alle bøker
            status = "Tilgjengelig" if book["availability"] else "Utlånt" # sjekke tilgjengelighet
            print(f'Tittel: {book["title"]}, Forfatter: {book["author"]}, Status: {status}') # skrive ut bokdetaljer

    def search_book(self, title): # metode for å søke etter en bok
        for book in self.data["books"]: # iterere gjennom alle bøker
            if book["title"].lower() == title.lower(): # sjekke om tittelen matcher (case-insensitive)
                status = "Tilgjengelig" if book["availability"] else "Utlånt" # sjekke tilgjengelighet
                print(f'Fant boken: {book["title"]} av {book["author"]} ({status})') # skrive ut bokdetaljer
                return
        print("Boken ble ikke funnet.") # hvis boken ikke ble funnet

    def checkout_book(self, title): # metode for å låne en bok
        for book in self.data["books"]: # iterere gjennom alle bøker
            if book["title"].lower() == title.lower(): # sjekke om tittelen matcher (case-insensitive)
                if book["availability"]: # sjekke om boken er tilgjengelig
                    book["availability"] = False # sette tilgjengelighet til false (utlånt)
                    save_library_data(self.file_path, self.data) # lagre endringer til fil
                    print(f'Du har lånt "{book["title"]}".') # bekreftelse på lån
                    return
                else:
                    print(f'Beklager, "{book["title"]}" er allerede utlånt.') # hvis boken er utlånt
                    return
        print("Boken finnes ikke.") # hvis boken ikke ble funnet

    def return_book(self, title): # metode for å returnere en bok
        for book in self.data["books"]: # iterere gjennom alle bøker
            if book["title"].lower() == title.lower():  # sjekke om tittelen matcher (case-insensitive)
                if not book["availability"]: # sjekke om boken er utlånt
                    book["availability"] = True # sette tilgjengelighet til true (tilgjengelig) 
                    save_library_data(self.file_path, self.data) # lagre endringer til fil
                    print(f'Du har levert tilbake "{book["title"]}".') # bekreftelse på
                    return
                else:
                    print(f'"{book["title"]}" var ikke utlånt.') # hvis boken ikke var utlånt
                    return
        print("Boken finnes ikke.") # hvis boken ikke ble funnet


# Hovedprogram med meny
def main(): # hovedfunksjon
    library = Library(file_path) # opprette bibliotek-objekt

    while True: # uendelig løkke for meny
        library_homepage() # vise hovedmeny
        choice = input("Velg et tall (1-5):") # be om brukerinput

        if choice == "1": # hvis valg er 1
            library.show_all_books() # vise alle bøker
        elif choice == "2": # hvis valg er 2
            title = input("Skriv inn boktittel du vil søke etter: ") # be om boktittel du vil søke etter
            library.search_book(title) # søke etter bok
        elif choice == "3": # hvis valg er 3
            title = input("Skriv inn boktittel du vil låne: ") # be om boktittel du vil låne
            library.checkout_book(title) # låne bok
        elif choice == "4": # hvis valg er 4
            title = input("Skriv inn boktittel du vil returnere: ") # be om boktittel du vil returnere
            library.return_book(title) # returnere bok
        elif choice == "5": # hvis valg er 5
            print("Avslutter programmet. Ha en fin dag!") # avslutningsmelding
            break
        else:
            print("Ugyldig valg, prøv igjen.") # hvis valg er ugyldig

if __name__ == "__main__": # sjekke om scriptet kjøres direkte
    main() # kjøre hovedfunksjonen