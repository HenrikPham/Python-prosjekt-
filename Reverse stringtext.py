     #lager en variabel kalt string som innholder inputet til brukeren#
string = input ("enter the word you like to reverse") 

#lager en funksjon som reverserer stringen#
def reverse (string) :

    #lager en tom variabel kalt revatering som skal innholde den reverserte stringen#
    revatering = ''

    #lager en variabel kalt index som skal telle nedover fra lengden av stringen til 0#
    index = len(string)

    #lager en while-løkke som legger til bokstavene i stringen i reversert rekkefølge til revatering#
    while index > 0 :

        #legger til bokstaven i stringen på plass index - 1 til revatering#
        revatering += string[index - 1]

        #reduserer index med 1#
        index = index - 1

    #returnerer den reverserte stringen#
    return revatering

#printer den reverserte stringen ved å kalle på funksjonen reverse og sende inn string som argument#
print (reverse(string))
