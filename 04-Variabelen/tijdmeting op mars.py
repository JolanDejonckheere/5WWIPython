#invoer
a = int(input('geef aantal sol:'))
sol = 88775.244
dag = 86400
uur = 3600
minuten = 60
seconden = 1
totaal_seconden = a * sol


#berekening
aantal_dagen = int(totaal_seconden // dag)
aantal_dagenseconden = int(aantal_dagen) * dag
totaal_seconden = totaal_seconden - int(aantal_dagenseconden)

aantal_uur = int(totaal_seconden // uur)
aantal_uurseconden = aantal_uur * uur
totaal_seconden = totaal_seconden - aantal_uurseconden

aantal_minuten = int(totaal_seconden // minuten)
aantal_minutenseconden = int(aantal_minuten) * minuten
totaal_seconden = totaal_seconden - aantal_minutenseconden

aantal_seconden = int(totaal_seconden // seconden)
totaal_seconden = totaal_seconden - int(aantal_seconden)

print(a, 'sol =', aantal_dagen, 'dagen,', aantal_uur, 'uren,', aantal_minuten, 'minuten en', aantal_seconden, 'seconden')


