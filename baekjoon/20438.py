import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
ks = [False] * (n + 3)
for i in map(int, input().split()):
    ks[i] = True

qs = [0] * (n + 3)
for i in map(int, input().split()):
    if ks[i]:
        continue
    for j in range(i, n + 3, i):
        if not ks[j]:
            qs[j] = 1

for i in range(2, len(qs)):
    qs[i] += qs[i - 1]
    
for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    print(e - s - (qs[e] - qs[s]))
