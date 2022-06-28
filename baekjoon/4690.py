def calculate(a):
    a3 = a ** 3
    for b in range(2, a):
        b3 = b ** 3
        for c in range(b + 1, a):
            c3 = c ** 3
            for d in range(c + 1, a):
                d3 = d ** 3
                if a3 == b3 + c3 + d3:
                    print('Cube = {0}, Triple = ({1},{2},{3})'.format(a, b, c, d))

for a in range(6, 101):
    calculate(a)