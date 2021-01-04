'''
In der Programmierung gibt es zwei grundsätzliche Strategien wie Werte 
von Variablen in Funktionen aufgerufen werden. Folgend sind diese Grundliegend erläutert.

Call-By-Value:
Wie in anderen Sprachen z.B. C/C++ werden hier zugewiesene Variablen in eine Funktion kopiert.
Dadurch sind die ursprünglichen Werte durch die Logik in der Funktion nicht modifizierbar.

Call-By-Reference:
Wie der Name schon sagt wird bei dieser Strategie eine direkte Referenz zu der Speicheradresse
des Wertes in die Funktion übergeben. Dies hat zufolge das die Logik einer Funktion den ursprünglichen 
Wert direkt verändert und keine Kopie erstellt. Diese Strategie wird von vielen Sprachen unterstützt 
aber nicht als Standard definiert. 

Jetzt ist die Frage: Wie ist es in Python? Schauen wir es uns an.
'''

# definieren wie ein Wert x = 42
x = 42

# definieren wir eine Funktion die x ausgibt
def f(x):
    # x = 5 <-- Ändert die Strategie von Referenz zu Value
    print('Der Wert von x ist: ', x)
    print('Die id von x in f() ist: ', id(x))

f(x)

# -> x hat die id (s. deine Ausgabe) in der Funktion f
# Was ist mit der id x außerhalb von f?
print('Die id von x ist: ', id(x)) # <-- id ist die gleiche!

'''
Die Strategie in Python ist eine kombination beider Strategien. So lange der Wert nur gelesen wird
und nicht verändert wird ist Call-By-Reference aktiv, jedoch wird bei Neuzuweisung ein neues Objekt erzeugt
(s. Kapitel OOP) und Call-By-Value wird aktiv.
'''