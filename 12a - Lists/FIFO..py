lijst = []
woord = input('geef woord')

while woord != 'STOP':
    if woord != '?':
        lijst.append(woord)
    elif len(lijst) > 0:
        print(lijst.pop(0))

    woord = input('geef woord')
