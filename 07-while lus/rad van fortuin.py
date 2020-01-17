verborgen_woord = input('geef verborgen woord')
gedraaide_geldbedrag = int(input('bedrag'))
letter = input('geef letter')

bedrag = 0
vorige_letter = ''

while letter in verborgen_woord and letter != vorige_letter:
    vorige_letter = letter
    bedrag += gedraaide_geldbedrag
    letter = input('geef nog een letter')

print(bedrag)
