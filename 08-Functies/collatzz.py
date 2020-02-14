def volgend_collatz_getal(n):
    if n * 2 == 0:
        uitkomst = n / 2
    else:
        uitkomst = (n * 3) + 1

    return uitkomst


def collatz(n):
    stappen = 1
    while n != 1:
        n = volgend_collatz_getal(n)
        stappen += 1

    return stappen

