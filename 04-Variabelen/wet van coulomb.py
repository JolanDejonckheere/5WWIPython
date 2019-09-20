#invoer
r = float(input('geef straal'))
r = r * 10**-2
q1 = 2.0 * 10**-6
q2 = 1.0 * 10**-6

#berekening
f_c = 8.99 * 10**9 * q1*q2 /r**2
#uitvoer
print(f_c)

