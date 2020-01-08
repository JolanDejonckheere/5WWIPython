aantal_seconden = int(input('geef aantal seconden'))

stappen = 0
vooruit = 0
achteruit = 0

for i in range(1, aantal_seconden + 1, 1):
    if i % 2 == 1:
        vooruit += 2
        stappen += vooruit

    else:
        achteruit += 1
        stappen -= achteruit

print(stappen)
