lijst = []
kleur = input('geef woord')

while kleur != 'STOP':
    if kleur != '?':
        lijst.append(kleur)
    elif len(lijst) > 0:
        print(lijst.pop(0))

    kleur = input('geef woord')


