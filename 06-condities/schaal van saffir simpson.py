#invoer
getal = int(input('geef een windsnelheid'))

#berekening
if getal >= 250:
    uitvoer = 'categorie 5'

elif getal >= 210:
    uitvoer = 'categorie 4'

elif getal >= 178:
    uitvoer = 'categorie 3'

elif getal >= 154:
    uitvoer = 'categorie 2'

elif getal >= 119:
    uitvoer = 'categorie 1'

else:
    uitvoer = 'geen orkaan'

#uitvoer
print(uitvoer)
