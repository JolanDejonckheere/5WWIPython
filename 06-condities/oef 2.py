getal = int(input('geef getal'))

if getal < 0 and getal %2 == 0:
    uitvoer = 'negatief en even getal'
elif getal < 0 and getal %2 != 0:
    uitvoer = 'negatief en oneven getal'
elif getal > 0 and getal % 2 == 0:
    uitvoer = 'positief en even getal'
elif getal > 0 and getal % 2 != 0:
    uitvoer = 'positief en oneven getal'
else:
    uitvoer = 'je getal is 0'

print(uitvoer)
