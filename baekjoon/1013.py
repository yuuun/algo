import re
isSpreaded = re.compile('(100+1+|01)+')
T = int(input())
for _ in range(T):
    st = input()
    m = isSpreaded.fullmatch(st)
    if m is None:
        print('NO')
    else:
        print("YES")