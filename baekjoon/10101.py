a, b, c =  int(input()), int(input()), int(input())

def chcktwo(a, b):
    if a == b:
        return True
    else: 
        return False

if a + b + c != 180:
    print('Error')
else:
    chAB, chBC, chCA = chcktwo(a, b), chcktwo(b, c), chcktwo(c, a)
    if chAB and chBC:
        print('Equilateral')
    elif chAB or chBC or chCA:
        print('Isosceles')
    else:
        print('Scalene')