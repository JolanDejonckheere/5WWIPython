#invoer
r = float(input(''))
R = float(input(''))
pi = 3.14159265359
#berekening
n = 0.83*R**2/r**2 - 1.9
n = int(n//1)

op_c1 = r**2 *pi
op_c2 = R**2 *pi
procent = ((n * op_c1) / op_c2) * 100
procent = round(procent, 2)
#uitvoer
print(n, 'kleine circels bedekken', procent, '% van de grote circel')




