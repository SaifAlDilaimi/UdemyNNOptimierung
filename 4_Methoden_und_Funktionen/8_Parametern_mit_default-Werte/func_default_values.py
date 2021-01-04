'''
Fortsetzung Video Funktion überladen: In Python wird das konzept der Überladung durch Parametern mit default-Werten ersetzt.

'''

# Lass uns die Funktion f  wieder anschauen. Die Problematik des Namens wird durch einen default-Wert ersetzt.
# def f():
    # print("Hallo Saif")

# Funktion f mit default-Wert
'''
def f(name='Saif'):
    print('Hallo '+name)

f()
f('Peter')
f('Jens')
'''
# Wie führen wir nun abhängig vom Parameter eine andere Logik?
def f(name='Saif'):
    if name == 'Saif':
        print('Hallo Lieber '+name)
    elif name == 'Peter':
        print('Hallo Dr. '+name)
    else:
        print('Hallo '+name)

f()
f('Peter')
f('Jens')