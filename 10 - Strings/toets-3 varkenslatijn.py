def verwijder_medeklinkers(woord):
    nieuw_woord = ''
    zoveelste_letter = 0
    for i in range(0, len(woord)):
        if woord[i] in 'aeiou':
            nieuw_woord += woord[zoveelste_letter:]
            return nieuw_woord
        else:
            zoveelste_letter += 1

def varkenslatijn(woord):
    nieuw_woord = ''
    for i in range(0, len(woord)):
        if woord[i] in 'aeiou':
            nieuw_woord += woord + 'ibus'
            nieuw_woord = nieuw_woord.replace('y', '')
            nieuw_woord = nieuw_woord.replace('z', '')
            return nieuw_woord.replace('j', 'i')
        elif woord[len(woord) - 1] in 'aiu':
            nieuw_woord += woord + 'nt'
            nieuw_woord = nieuw_woord.replace('y', '')
            nieuw_woord = nieuw_woord.replace('z', '')
            return nieuw_woord.replace('j', 'i')
        else:
            nieuw_woord += verwijder_medeklinkers(woord) + 'itum'
            nieuw_woord = nieuw_woord.replace('y', '')
            nieuw_woord = nieuw_woord.replace('z', '')
            return nieuw_woord.replace('j', 'i')




def vertaal(zin):

    return varkenslatijn(zin)











