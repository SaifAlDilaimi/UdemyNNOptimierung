'''
Rekursive Funktionen ist eine Art von Programmierung, welches darauf basiert, dass 
die Funktion sich selbst innerhalb ihrer Logik aufruft. Dies ermöglicht die vermeidung von 
Schleifen für einen sich wiederholenden Prozess. 

Beispiel:

4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1

-> 4! = 4 * 3 * 2 * 1

Wir versuchen immer kleiner Stück eines Problem zu lösen! Lass uns 4! berechnen.

Formel: n! = n * (n - 1), falls n > 1 und 0! = 1
'''

# Lass uns iterative 4! berechnen
def iterative_fakultaet(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        print(result)
    return result

iterative_fakultaet(4)

# Nun Rekursiv!
def recursive_fakultaet(n):
    print('Rekursive Funktion aufgerufen für n = ' + str(n))
    if n == 0:
        return 1
    else:
        res = n * recursive_fakultaet(n - 1)
        print('Ergebnis für zwischenschritt: ', res)
        return res

print(recursive_fakultaet(4))