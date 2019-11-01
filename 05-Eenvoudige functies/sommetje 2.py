#invoer
x = int(input('geef getal 1'))
y = int(input('geef getal 2'))

#uitvoer

print('{:>9d} + {:<9d}'.format(x, y), '=', x + y)
print('{:>9d} + {:<9d}'.format(10*x, 10*y), '=', 10*x + 10*y)
print('{:>9d} + {:<9d}'.format(100*x, 100*y), '=', 100*x + 100*y)
print('{:>9d} + {:<9d}'.format(1000*x, 1000*y), '=', 1000*x + 1000*y)
print('{:>9d} + {:<9d}'.format(10000*x, 10000*y), '=', 10000*x + 10000*y)

