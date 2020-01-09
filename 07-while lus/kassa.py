productprijs = float(input(''))
totaal = productprijs

while productprijs != 0:
    productprijs = float(input(''))
    totaal += productprijs

print('De totale prijs is €', "{:.2f}".format(totaal))


