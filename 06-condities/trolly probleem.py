antw1 = input('aan hendel trekken?')
antw2 = input('man over brug duwen')

if antw1 == 'ja' and antw2 == 'ja':
    doden = 2

elif antw1 == 'ja' and antw2 == 'nee':
    doden = 1

elif antw1 == 'nee' and antw2 =='ja':
    doden = 1

elif antw1 == 'nee' and antw2 == 'nee':
    doden = 5

print(doden)



