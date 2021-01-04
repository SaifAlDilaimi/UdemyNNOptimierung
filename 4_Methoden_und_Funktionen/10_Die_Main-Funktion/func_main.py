'''
Bisher wurde unser Quellcode Sequentiell abgearbeitet. Nun möchten wir uns die 
Main-Funktion anschauen: Der Startpunkt eines Python-Programms.
'''

# Lass uns eine Funktion add definieren
def add(a, b):
    return a + b

# Lass uns eine Funktion main definieren
def main():
    a = 5
    b = 7
    c = add(a, b)
    print('Das Ergebnis von a + b ist: ', c)

if __name__ == '__main__':
    main() # Jegliche weitere Logik wird in dieser Funktion ausgeführt

'''
Durch die Main-Funktion stellen wir ein Einstiegspunkt für unser Programm. Die Main-Funktion 
enthält alles weitere an Logik. Weitere Funktionen wie add sollten auserhalb der Main-Funktion definiert werden.
Dies führt dazu, dass wir auch später (bei Module) Modular Funktionen aufrufen können.
'''