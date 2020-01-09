aantal = int(input('geef aantal basen'))

base_1 = ''
base_2 = ''
base_3 = ''
base_4 = ''

for i in range(1, aantal + 1):
    base = input('geef base')
    if base == 'A':
        base_1 = 'A'
    elif base == 'C':
        base_2 = 'C'
    elif base == 'G':
        base_3 = 'G'
    else:
        base_4 = 'T'

verschillende_basen = int(len(str(base_1 + base_2 + base_3 + base_4)))

if verschillende_basen == 1:
    print('De DNA-keting bevat 1 soort base:', base_1, base_2, base_3, base_4)
else:
    print('De DNA-keting bevat', verschillende_basen, 'verschillende soorten basen:', base_1, base_2, base_3, base_4)




