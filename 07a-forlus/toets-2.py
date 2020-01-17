getal1 = int(input('geef getal 1'))
getal2 = int(input('geef getal 2'))

som1, som2 = 0, 0

for i in range(2, getal1 + 1):
    if getal1 % i == 0:
        som1 += getal1 / i

for i in range(2, getal2 + 1):
    if getal2 % i == 0:
        som2 += getal2 / i

if getal1 == som2 and getal2 == som1:
    print('{} en {} zijn bevriende getallen'.format(getal1, getal2))
else:
    print('{} en {} zijn geen bevriende getallen'.format(getal1, getal2))

