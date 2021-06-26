#TBD
n, k, m = map(int, input().split())
lis = [i for i in range(1, n+1)]
cur = k - 1

tmp = k - 1

res = [lis.pop(cur)]
isRotate = True
while lis:
    if len(res) % m == 0:
        isRotate = not isRotate
    if isRotate:
        cur = (cur + k - 1) % len(lis)
    else:
        cur = (cur - k) % len(lis)
        while cur < 0:
            cur += len(lis)
    res.append(lis.pop(cur))

print("\n".join(map(str, res)))