n = int(input(''))

getal_1 = 1
getal_2 = 1

if n <= 2:
    getal = 1
else:
    for i in range(n-2):
        getal = getal_1 + getal_2
        getal_1 = getal_2
        getal_2 = getal

print(getal)
