import re
r = re.compile('(100+1+|01)+')
if r.fullmatch(input()):
    print('SUBMARINE')
else:
    print('NOISE')