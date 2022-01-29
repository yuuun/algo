a, b, c = map(int, input().split())

while not (a == b == c == 0):
    if a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
        
    a, b, c = map(int, input().split())