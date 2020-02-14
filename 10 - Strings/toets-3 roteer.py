def roteer(woord, n):
    nieuw_woord = ''
    for i in range(0, len(woord)):
        nieuw_woord += woord[(i + n) % len(woord)]

    return nieuw_woord









