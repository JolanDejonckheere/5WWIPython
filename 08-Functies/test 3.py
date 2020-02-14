from random import randint



def gooi_muntstuk():
    muntstuk = 'munt'
    if not randint(0, 2):
        muntstuk = 'kop'
    return muntstuk


a = 4
for i in range(10):
    print(gooi_muntstuk())
#print(rg, muntstuk)


