n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]

cand = []
s = li[0]
for _ in range(n):
    cand.append(s)
    e = li[s]
    cand.append(e)
    s = li[e]

if k in cand:
    print(cand.index(k) + 1)
else:
    print(-1)