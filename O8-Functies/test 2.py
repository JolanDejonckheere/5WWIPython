from math import sqrt




def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def wortels(a, b, discriminant):
   w1, w2 = None, None
    d = discriminant(a, b, c)
    if d >= 0:
        w1 = (-b + sqrt(d)) / (2 * a)
        w2 = (-b - sqrt(d)) / (2 * a)
    return w1, w2


# ax^2 + bx + c = 0
# 2x^2 - x + 4 = 0
wortel1, wortel2 = wortels(4,8,4)
print(wortel1, wortel2)


