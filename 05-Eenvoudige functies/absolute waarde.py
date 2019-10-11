#invoer
x = float(input(''))
y = float(input(''))

#berekening
opl1 = abs(abs(x) - abs(y))
opl2 = abs(x - y)

opl1 = round(opl1, 4)
opl2 = round(opl2, 4)


print(str(opl1) + ' \N{LESS-THAN OR EQUAL TO} ' + str(opl2))

