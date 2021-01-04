'''
Inner/Nested Funktionen ermöglichen uns unseren Code zu verbessern, indem wir Helfer-Funktionen nur in den notwendigen
Kontext anzubieten.

'''

# Als Beispiel wollen wir eine Funktionen schreiben die uns
# die Fakultät berechnet
# Beispiel 4! = 1 * 2 * 3 * 4 = 24

def fakultaet(n):

    # Error abfangen
    if n < 0:
        print("Sorry. 'n' muss >= 0 sein.")
        exit()


    def inner_fakultaet(n):
        if n <= 1:
            return 1
        return n * inner_fakultaet(n-1)

    return inner_fakultaet(n)

# outer function aufrufen.
print(fakultaet(4))