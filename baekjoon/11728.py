n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ta, tb = 0, 0
c = []
while ta < n and tb < m:
    if a[ta] > b[tb]:
        c.append(b[tb])
        tb += 1
    elif a[ta] < b[tb]:
        c.append(a[ta])
        ta += 1
    else:
        c.append(a[ta])
        c.append(b[tb])
        ta += 1
        tb += 1
while ta < n:
    c.append(a[ta])
    ta += 1
while tb < m:
    c.append(b[tb])
    tb += 1

print(' '.join(map(str, c)))