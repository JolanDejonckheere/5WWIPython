#invoer
dag = int(input('geef een dag'))
maand = int(input('geef een maand'))
jaar = int(input('geef een jaar'))

if jaar // 4 and not jaar // 400 and jaar//100:
    if maand == 2:
        if dag == 29:
            dag = 1
            maand += 1
        else:
            dag += 1

    elif maand == 12:
        if dag == 31:
            dag = 1
            maand = 1
            jaar += 1
        else:
            dag += 1

    elif maand == 1 or 3 or 5 or 7 or 8 or 10:
        if dag == 31:
            dag = 1
            maand += 1
        else:
            dag += 1
    else:
        if dag == 30:
            dag = 1
            maand += 1

else:
    if maand == 2:
        if dag == 28:
            dag = 1
            maand += 1
        else:
            dag += 1

    elif maand == 12:
        if dag == 31:
            dag = 1
            maand = 1
            jaar += 1
        else:
            dag += 1

    elif maand == 1 or 3 or 5 or 7 or 8 or 10:
        if dag == 31:
            dag = 1
            maand += 1
        else:
            dag += 1
    else:
        if dag == 30:
            dag = 1
            maand += 1

print(str(dag) + '/' + str(maand) + '/' + str(jaar))
