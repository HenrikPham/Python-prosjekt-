import tkinter as tk # for GUI
from tkinter import messagebox, simpledialog, ttk # for GUI-komponenter
import json, os # for filhåndtering

file_path = "data_GUI.json" # filsti for lagring av data

# data storage 
library_data = {"books": [ # liste over bøker i biblioteket
    # tittel, forfatter, tilgjengelighet
    {"title": "1984", "author": "George Orwell", "availability": True }, # true = tilgjengelig, false = utlånt
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "availability": False }, # utlånt
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "availability": True }, # tilgjengelig
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "availability": True }, # tilgjengelig
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "availability": False }, # utlånt
    {"title": "Pride and Prejudice", "author": "Jane Austen", "availability": True }, # tilgjengelig
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "availability": True }, # tilgjengelig
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "availability": False }, # utlånt
    {"title": "Animal Farm", "author": "George Orwell", "availability": True }, # tilgjengelig
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "availability": True }, # tilgjengelig
    {"title": "Cat Warriors", "author": "Erin Hunter", "availability": True }  # tilgjengelig
]} 

def load_library_data(file_path): # funksjon for å laste bibliotekdata fra fil
    if os.path.exists(file_path): # sjekke om filen eksisterer
        with open(file_path, 'r', encoding='utf-8') as f: # åpne fil i lese-modus
            return json.load(f) # returnere data fra fil
    else:
        return {"books": []} # returnere tom liste hvis filen ikke eksisterer
    
def save_library_data(file_path, data): # funksjon for å lagre bibliotekdata til fil
    with open(file_path, 'w', encoding='utf-8') as f: # åpne fil i skrive-modus
        json.dump(data, f, ensure_ascii=False, indent=2) # lagre data til fil

# Bilbliotekshjememeside
def library_homepage(): # funksjon for å vise hovedmenyen
    print("Velkommen til Biblioteket!") # velkomstmelding
    print("1. Legg til bok") # menyvalg 1 - legg til en bok
    print("2. Vis alle bøker") # menyvalg 2 - vis alle bøker
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
        return self.data["books"] # returnere liste over alle bøker

    def add_book(self, title, author,): # metode for å legge til en bok
        if not title.strip() or not author.strip(): # sjekke om tittel eller forfatter er tom
            return False, "Tittel og forfatter kan ikke være tomme!" # returnere feilmelding
        for book in self.data["books"]: # sjekke om boken allerede finnes
            if book["title"].lower() == title.lower(): # sammenligne titler uten å ta hensyn til store/små bokstaver
                return False, f'Boken "{title}" finnes allerede!' # returnere feilmelding
        new_book = {"title": title, "author": author, "availability": True} # opprette ny bok
        self.data["books"].append(new_book) # legge til ny bok i listen
        save_library_data(self.file_path, self.data) # lagre endringer til fil
        return True, f'Boken "{title}" av {author} er lagt til i biblioteket.' # bekreftelse på at boken er lagt til

    def checkout_book(self, title): # metode for å låne en bok
        for book in self.data["books"]: # iterere gjennom alle bøker
            if book["title"].lower() == title.lower(): # sjekke om tittelen matcher (case-insensitive)
                if book["availability"]: # sjekke om boken er tilgjengelig
                    book["availability"] = False # sette tilgjengelighet til false (utlånt)
                    save_library_data(self.file_path, self.data) # lagre endringer til fil
                    return True # bekreftelse på lån
                else: 
                    return False # hvis boken er utlånt year
        return None # hvis boken ikke ble funnet

    def return_book(self, title): # metode for å returnere en bok
        for book in self.data["books"]: # iterere gjennom alle bøker
            if book["title"].lower() == title.lower(): # sjekke om tittelen matcher (case-insensitive)
                if not book["availability"]: # sjekke om boken er utlånt
                    book["availability"] = True # sette tilgjengelighet til true (tilgjengelig)
                    save_library_data(self.file_path, self.data) # lagre endringer til fil
                    return True # bekreftelse på retur
                else: 
                    return False # hvis boken ikke var utlånt
        return None # hvis boken ikke ble funnet


# GUI med Tkinter
class LibraryGUI: # klasse for GUI
    def __init__(self, root, library): # initialiseringsmetode
        self.library = library # lagre bibliotek-objekt
        self.root = root # lagre root-objekt
        self.root.title("Biblioteksystem") # sette vindustittel


        tk.Label(root, text="Velkommen til Biblioteket!", font=("Helvetica", 16)).pack(pady=10) # velkomstmelding


        self.search_var = tk.StringVar() # variabel for søkefelt
        self.search_var.trace("w", self.update_book_list) # oppdatere bokliste ved endring i søkefelt


        self.filter_var = tk.StringVar() # variabel for filter
        self.filter_box = ttk.Combobox(root, textvariable=self.filter_var, # dropdown for filter
                                        values= ["Alle", "Tilgjengelige", "Utlånte"], # alternativer
                                        state="readonly") # kun lesbar
        self.filter_box.current(0) # sette standardverdi til "Alle"   
        self.filter_box.pack() # pakke inn i vinduet
        self.filter_box.bind("<<ComboboxSelected>>", lambda e: self.update_book_list()) # oppdatere bokliste ved valg i dropdown                                 


        # Liste over bøker
        self.listbox = tk.Listbox(root, width=80, height=20) # listeboks for å vise bøker
        self.listbox.pack(pady=10) # pakke inn i vinduet
        self.update_book_list() # initialisere bokliste


        # Søkefelt
        self.entry = tk.Entry(root, textvariable=self.search_var, width=40) # inndatafelt for søk
        self.entry.pack() # pakke inn i vinduet


        # Knapper 
        tk.Button(root, text="Legg til bok", command=self.add_book).pack(pady=2) # knapp for å legge til bok
        tk.Button(root, text="Lån bok", command=self.checkout_book).pack(pady=2) # knapp for å låne bok
        tk.Button(root, text="Returner bok", command=self.return_book).pack(pady=2) # knapp for å returnere bok
        tk.Button(root, text="Avslutt", command=root.quit).pack(pady=2) # knapp for å avslutte programmet


    def update_book_list(self, *args): # oppdatere bokliste basert på søk og filter|
        self.listbox.delete(0, tk.END) # tømme liste
        filter_val = self.filter_var.get() # hente filterverdi
        search_text = self.search_var.get().lower() # hente søketekst og gjøre den til små bokstaver

        for book in self.library.show_all_books(): # iterere gjennom alle bøker
            status = "Tilgjengelig" if book["availability"] else "Utlånt" # sjekke tilgjengelighet
            if filter_val == "Tilgjengelige" and not book["availability"]: # hvis filter er "Tilgjengelige" og boken ikke er tilgjengelig
                continue # hoppe over denne boken
            if filter_val == "Utlånte" and book["availability"]: # hvis filter er "Utlånte" og boken er tilgjengelig
                continue # hoppe over denne boken
            if search_text and search_text not in book["title"].lower() and search_text not in book["author"].lower(): # hvis søketekst ikke er tom og ikke finnes i tittel eller forfatter
                continue # hoppe over denne boken

            self.listbox.insert(tk.END, f'{book["title"]} av {book["author"]} ({status})') # legge til bok i liste


    def add_book(self):
        title = simpledialog.askstring("Legg til bok", "Skriv inn boktittel:")
        if not title: return
        author = simpledialog.askstring("Legg til bok", "Skriv inn forfatter:")
        if not author: return
        success, message = self.library.add_book(title, author,)
        if success:
            messagebox.showinfo("Suksess", message)
        else:
            messagebox.showwarning("Feil", message)
        self.update_book_list()


    def checkout_book(self):
        try:
            # få indeksen til markert bok
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Ingen bok valgt", "Vennligst velg en bok fra listen.")
            return

        # hent boktittel fra listen
        book_text = self.listbox.get(index)
        title = book_text.split(" av ")[0]  # splitter for å få tittel før ' av '

        # lån boka
        result = self.library.checkout_book(title)
        if result is True:
            messagebox.showinfo("Suksess", f'Du har lånt "{title}".')
        elif result is False:
            messagebox.showwarning("Opptatt", f'"{title}" er allerede utlånt.')
        else:
            messagebox.showerror("Feil", "Boken finnes ikke.")

        self.update_book_list()
 

    def return_book(self):
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Ingen bok valgt", "Vennligst velg en bok fra listen.")
            return

        book_text = self.listbox.get(index)
        title = book_text.split(" av ")[0]

        result = self.library.return_book(title)
        if result is True:
            messagebox.showinfo("Suksess", f'Du har levert tilbake "{title}".')
        elif result is False:
            messagebox.showwarning("Ikke utlånt", f'"{title}" var ikke utlånt.')
        else:
            messagebox.showerror("Feil", "Boken finnes ikke.")

        self.update_book_list()


# Hovedprogram med meny
def main(): # hovedfunksjon
    library = Library(file_path) # opprette bibliotek-objekt
    while True: # hoved løkke
        library_homepage() # vise hovedmeny
        choice = input("Velg et alternativ (1-5): ") # be om valg
        if choice == '1':
            title = input("Skriv inn boktittel: ") # be om boktittel
            author = input("Skriv inn forfatter: ") # be om tittel og forfatter
            success, message = library.add_book(title, author) # legge til bok
            print(message) # bekreftelse på at boken er lagt til
        elif choice == '2': 
            for book in library.show_all_books(): # vise alle bøker
                status = "Tilgjengelig" if book["availability"] else "Utlånt" # sjekke tilgjengelighet
                print(f'{book["title"]} av {book["author"]} {status}') # vise alle bøker
        elif choice == '3':
            title = input("Skriv inn boktittel du vil låne: ") # be om boktittel
            result = library.checkout_book(title) # låne bok
            if result is True:
                print(f'Du har lånt "{title}".') # bekreftelse på lån
            elif result is False:
                print(f'"{title}" er allerede utlånt.') # hvis boken er utlånt
            else:
                print("Boken finnes ikke.") # hvis boken ikke ble funnet
        elif choice == '4': 
            title = input("Skriv inn boktittel du vil returnere: ") # be om boktittel
            result = library.return_book(title) # returnere bok
            if result is True: 
                print(f'Du har levert tilbake "{title}".') # bekreftelse på
            elif result is False: 
                print(f'"{title}" var ikke utlånt.') # hvis boken ikke var utlånt
            else:
                print("Boken finnes ikke.") # hvis boken ikke ble funnet
        elif choice == '5': 
            print("Takk for at du brukte biblioteket. Ha en fin dag!") # avslutningsmelding
            break # avslutte løkken og programmet


# Kjør GUI
if __name__ == "__main__": # sjekke om filen kjøres direkte
    mode = input("Vil du bruke GUI (g) eller tekst-meny (t)?") # be om valg av modus
    if mode.lower() == 'g': # GUI-modus
        root = tk.Tk() # opprette hovedvindu
        root.title("Biblioteksystem")
        root.geometry("450x300")
        library = Library(file_path) # opprette bibliotek-objekt
        gui = LibraryGUI(root, library) # opprette GUI-objekt
        root.mainloop() # starte GUI-løkken
    else: # tekst-meny
        main() # kjøre hovedprogrammet hvis filen kjøres direkte
