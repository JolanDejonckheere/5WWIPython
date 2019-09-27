#invoer
a = int(input('geef een geheel aantal seconden'))

dag = 86400
uur = 3600
minuut = 60
second = 1
totaal_seconden = a

#berekening

aantal_dagen = int(totaal_seconden // dag)
aantal_dagenseconden = aantal_dagen * dag
totaal_seconden -= aantal_dagenseconden

aantal_uren = int(totaal_seconden // uur)
aantal_urenseconden = aantal_uren * uur
totaal_seconden -= aantal_urenseconden

aantal_minuten = int(totaal_seconden // minuut)
aantal_minutenseconden = aantal_minuten * minuut
totaal_seconden -= aantal_minutenseconden

aantal_seconden = int(totaal_seconden // second)
aantal_secondenseconden = aantal_seconden * second
totaal_seconden -= aantal_secondenseconden

#uitvoer
print(str(aantal_dagen) + 'd ' + str(aantal_uren) + ':' + str(aantal_minuten) + ':' + str(aantal_secondenseconden))


