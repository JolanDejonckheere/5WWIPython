#invoer
aantal_seconden = int(input('geef een geheel getal'))

#berekening
dagen = aantal_seconden // 86400
aantal_seconden = aantal_seconden % 86400

uren = aantal_seconden // 3600
aantal_seconden = aantal_seconden % 3600

minuten = aantal_seconden // 60
aantal_seconden = aantal_seconden % 60

#uivoer
print(str(dagen) + 'd ' + str(uren) + ':' + str(minuten) + ':' + str(aantal_seconden))



