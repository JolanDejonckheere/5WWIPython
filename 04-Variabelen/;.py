input = int(input("geef aantal seconden"))
aantal_seconden = input

aantal_dagen = aantal_seconden // 86400
aantal_seconden = aantal_seconden % 86400

aantal_uren = aantal_seconden // 3600
aantal_seconden = aantal_seconden % 3600

aantal_minuten = aantal_seconden // 60
aantal_seconden = aantal_seconden % 60

print(input, "seconden is gelijk aan", aantal_dagen, "dag(en),", aantal_uren, "uur/uren,", aantal_minuten, "minuten,", aantal_seconden, "seconden")

