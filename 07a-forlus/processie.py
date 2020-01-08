tijd = int(input('geef tijd'))

stappen_vooruit = 2
stappen_achteruit = 0

for i in range(1, tijd + 1):
    aantal_stappen = stappen_vooruit - stappen_achteruit

    if i //2:
        stappen_vooruit += 2
    else:
        stappen_achteruit += 1




print(aantal_stappen)
