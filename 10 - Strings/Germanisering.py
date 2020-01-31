# --> werk met nieuwe_zin += ...
def germaniseer(zin):
    nieuwe_zin = ''
    #overloop alle letters van de string
    for i in range(0, len(zin)):
        #indien de letter een spatie is
        if zin[i] == ' ':
            # volgende letter wordt een hoofletter
            nieuwe_zin += ' ' + zin[i + 1].upper()
        elif zin[i - 1] != ' ':
            nieuwe_zin += zin[i]


        # plak aan nieuwe zin
    return nieuwe_zin

print(germaniseer('dit is een test'))

