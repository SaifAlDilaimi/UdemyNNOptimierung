'''
Mithilfe von Closure wird uns ermöglicht eine Art von Flexibilität zu gewährleisten ohne mehrere Funktionen zu definieren!

'''

'''
Als Beispiel wollen wir ein Closure erstellen der uns ermöglicht eine beliebige Zahl x mit 
einem der folgenden n zu Multiplizieren.

n :=  2, 4, 6
'''

# Wir Nutzen Nested/Inner Funktionen!
def make_multiplier_of(n):
    
    def multiply(x): 
        return x * n

    return multiply # Hier geben ein Closure zurück!

# Jetzt definieren wir unsere Closure
times2 = make_multiplier_of(2)
times4 = make_multiplier_of(4)
times6 = make_multiplier_of(6)

print(times2(5))
print(times4(5))
print(times6(5))

'''
Wann nutzt man Closures? 

- Wenn globale Variablen vermeidet werden soll
- Wenn eine Logik auf verschieden Werte angewandt werden soll
'''