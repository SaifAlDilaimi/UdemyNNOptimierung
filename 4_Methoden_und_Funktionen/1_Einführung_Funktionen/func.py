# Gebe deinen Namen aus
name = 'Saif'
print("Mein Name ist: ", name)

# wie würdest du diesen abschnitt "wiederholbar/dynamischer" machen?
# Lösung: Funktionen

'''
def funktionsname(param1, param2):
    logik..
'''
def name_ausgeben(name):
    print("Mein Name ist: ", name)

name_ausgeben('Saif')
name_ausgeben('Jan')
name_ausgeben('Müller')