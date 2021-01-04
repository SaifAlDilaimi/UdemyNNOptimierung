# Eine unbekannte Anzahl von Parametern
def prozentwert(**werte):
    print(werte, type(werte))

    p_satz = werte['psatz']
    g_wert = werte['gwert']

    p_wert = p_satz * g_wert / 100

    return p_wert
    



result = prozentwert(psatz=13, gwert=1000)
print(result)

