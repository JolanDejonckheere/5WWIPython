#invoer
thuis = float(input('score van de thuisploeg'))
uit = float(input('score van de uitploeg'))

print(thuis, uit)
verschil = abs(thuis - uit)


if thuis > uit:
    if verschil < 10:
        thuis = 600 - 70
        uit = 400 + 70
    elif verschil <= 20:
        thuis = 700 - 70
        uit = 300 + 70
    else:
        thuis = 800 - 70
        uit = 200 + 70

else:
    if verschil < 10:
        uit = 600 + 70
        thuis = 400 - 70
    elif verschil <= 20:
        uit = 700 + 70
        thuis = 300 - 70
    else:
        uit = 800 + 70
        thuis = 200 - 70

print(thuis)
print(uit)







