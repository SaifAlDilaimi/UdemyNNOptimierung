'''
Je nach Szenario ist es evtl. notwendig dynamisch Variablen zu setzen. Das bedeutet 
Nutzereingaben sollen möglich sein. 

Szenario: Alter des Nutzers erfragen statisch vs. dynamisch
'''

# statisch
alter = 27 # erfragt und festgelegt
print(alter, type(alter))

# dynamisch
alter = input('Bitte gib dein Alter ein: ')
print(alter, type(alter))

# alter von string zu int casten
alter = int(alter)
print(alter, type(alter))