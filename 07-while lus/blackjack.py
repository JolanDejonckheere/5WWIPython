kaart = int(input(''))
som = kaart

while som < 21 and kaart != 0:
    kaart = int(input(''))
    som += kaart

if som ==21:
    print('Gewonnen!')
elif som > 21:
    print('Verbrand (' + str(som) + ')')
else:
    print('Voorzichtig gespeeld (' + str(som) + ')')


