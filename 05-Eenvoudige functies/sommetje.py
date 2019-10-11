#invoer
x = int(input(''))
y = int(input(''))

#berekening
op1 = x + y
op2 = (10*x) + (10*y)
op3 = (100*x) + (100*y)
op4 = (1000*x) + (1000*y)
op5 = (10000*x) + (10000*y)
#uitvoer
print('   ', str(x), '+', str(y), '=', op1 )
print('  ', str(10*x), '+', str(10*y), '=', op2)
print(' ', str(100*x), '+', str(100*y), '=', op3)
print('', str(1000*x), '+', str(1000*y), '=', op4)
print(str(10000*x), '+', str(10000*y), '=', op5)
