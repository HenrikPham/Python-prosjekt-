#Lager en string som inneholder input fra brukeren#
string = input ("enter the word you like to analyze: ")

#Lager en funksjon som analyserer stringen#
def analyze (string) : 

    #Lager en variabler som skal telle antall bokstaver, mellomrom, ord og vokaler (a, e, i, o, u, y, æ, ø, å) i stringen#
    Letter_count = 0
    Spaces_count = 0
    Word_count = 0
    vowel_count = 0

    #Lager en for-løkke som går gjenom hver bokstav i stringen#
    for letter in string : 

        #Hvis bokstaven er en mellomrom, øker Spaces_count med 1#
        if letter == ' ' :
            Spaces_count += 1
            Letter_count -= 1 #Mellomrom teller ikke som en bokstav, så Letter_count reduseres med 1#
        
        #Hvis bokstaven er en vokal, øker vowel_count med 1#
        elif letter in 'aeiouyæøåAEIOUYÆØÅ' :
            vowel_count += 1

        #Uansett hvilken bokstav det er, øker Letter_count med 1#
        Letter_count += 1

    #Lager en variabel Word_count som teller antall ord i stringen ved å splitte stringen på mellomrom#
    words_split = string.split()
    Word_count = len(words_split)

    #Returnerer en tuple som inneholder antall bokstaver, mellomrom, ord og vokaler i stringen#
    return (Letter_count, Spaces_count, Word_count, vowel_count)

#Printer resultatet av å kalle på funksjonen analyze og sende inn string som argument#
print (analyze(string))
#Aktiverer funksjonen analyze og sender inn string som argument, og printer resultatet#
all = analyze(string)
print(f"vi har {all[0]} bokstaver, {all[1]} mellomrom, {all[2]} ord, {all[3]} vokaler i stringen.")