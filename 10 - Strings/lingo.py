def hint(gok, juiste_woord):
    hint = ''
    for i in range(len(juiste_woord)):
        if gok[i] in juiste_woord:
            if gok[i] == juiste_woord[i]:
                hint += gok[i].upper()
            else:
                hint += gok[i]
        else:
            hint = hint + '.'
    return hint


