brutoloon = float(input('geef brutoloon'))

round(brutoloon, 2)

rsz = (brutoloon / 100) * 13.07

netto = brutoloon - rsz

if netto <= 13250.00:
    schijf1 = netto
elif netto <= 23390.00:
    schijf1 = 13250.00
    schijf2 = netto - 13250.00
    schijf3 = 0.00
    schijf4 = 0.00
elif netto <= 40480.00:
    schijf1 = 13250.00
    schijf2 = 10140.00
    schijf3 = netto - 13250.00 - 10140.00
    schijf4 = 0.00
else:
    schijf1 = 13250.00
    schijf2 = 10140.00
    schijf3 = 17090.00
    schijf4 = netto - 13250.00 - 10140.00 - 1790.00

if schijf1 <= 8600.00:
    voorheffing = 0.00

if schijf1 <= 13250.00:
    voorheffing = ((schijf1-8600.00) / 100) * 25

if schijf2 <= 10140.00:
    voorheffing = (schijf2 / 100) * 40 + voorheffing

if schijf3 <= 17090:
    voorheffing3 = (schijf3 / 100) * 45 + voorheffing

if schijf4 > 0:
    voorheffing = (schijf4 / 100) * 50 + voorheffing

netto_jaarsalaris = netto - voorheffing
netto_maandsalaris = netto_jaarsalaris / 12



print('+ bruto jaarsalaris', brutoloon)
print('- rsz              ', rsz)
print('- voorheffingcccccc', voorheffing)
print('=================================')
print('{:.2f}'.format(netto_jaarsalaris))
print('{:.2f}'.format(netto_maandsalaris))







