def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')

def roteer_letter(letter, plaatsen):
    # volgnummer in alfabet bepaald van de gegeven letter
    volgnummer_letter = min(ord(letter) % ord('a'), ord(letter) % ord('A'))
    # volgnummer in alfabet van nieuwe letter
    nieuw_volgnummer = (volgnummer_letter + plaatsen) % 26
    # offset
    offset = nieuw_volgnummer - volgnummer_letter
    return chr(ord(letter) + offset)


def versleutel(zin, plaatsen):
    uitkomst = ''
    for letter in zin:
        uitkomst += roteer_letter(letter, plaatsen)

    return uitkomst








