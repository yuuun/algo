def calculateC(x, y, w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    c = h1 * h2 / (h1 + h2)
    return c

x, y, c = map(float, input().split())
start, end = 0, min(x, y)
res = 0
while end - start > 1e-6:
    mid = (start + end) / 2
    if calculateC(x, y, mid) >= c:
        res = mid
        start = mid
    else:
        end = mid
        
print('{:.3f}'.format(res))