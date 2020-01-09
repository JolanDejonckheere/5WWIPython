verborgen_woord = input('geef verborgen woord')
gedraaide_geldbedrag = int(input('bedrag'))
letter = input('geef letter')

bedrag = 0

while letter in verborgen_woord:
    letter = input('geef nog een letter')
    bedrag += gedraaide_geldbedrag

print(bedrag)
