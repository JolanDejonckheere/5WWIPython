def hoogtemeters(lijst):
    res = []

    for i in range(len(lijst) - 1):
        res.append(lijst[i + 1] - lijst[i])

    return res

def dalen_en_stijgen(lijst):
    dalen, stijgen = 0, 0
    for hoogtemeter in lijst:
        if hoogtemeter > 0:
            stijgen += hoogtemeter
        else:
            dalen += hoogtemeter

    return abs(dalen), stijgen






