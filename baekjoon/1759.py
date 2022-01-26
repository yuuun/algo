from itertools import combinations
l, c = map(int, input().split())
fig = sorted(input().split())

candidate = combinations(fig, l)
can = []
for cand in candidate:
    can.append(cand)

for c in can:
    cnt = 0
    if 'a' in c:
        cnt += 1
    if 'e' in c:
        cnt += 1
    if 'i' in c:
        cnt += 1
    if 'o' in c:
        cnt += 1
    if 'u' in c:
        cnt += 1
    if  l - 1 > cnt > 0:
        print(''.join(c))