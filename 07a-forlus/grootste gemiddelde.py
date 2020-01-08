aantal = int(input('aantal getallen'))

# lees het eerste getal voor de lus in
getal_0 = int(input('geef getal : '))

# Het eerste getal is onmiddelijk de som en het grootste getal
som, grootste = getal_0, getal_0

for i in range(aantal - 1):
    getal = int(input('geef getal' + str(i + 1) + ':'))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal

gemiddelde = '{:.2f}'.format(gemiddelde)

print('Het grootste getal is', grootste, 'en het gemiddelde is', gemiddelde)


