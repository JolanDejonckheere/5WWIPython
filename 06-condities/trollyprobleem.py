hendel_trekken = input('aan de hendel trekken')
man_duwen = input('man duwen')

if hendel_trekken == 'ja' and man_duwen == 'ja':
    doden = 2
elif hendel_trekken == 'ja' and man_duwen != 'ja':
    doden = 5
else:
    doden = 1

print(doden)
