from collections import deque
n, k = map(int, input().split())
loc = list(map(int, input().split()))
visited = set()

q = deque()
for l in loc:
    q.append([l, 1])
    visited.add(l)

res, m = 0, 0

while q:
    t, cnt = q.popleft()
    for x in [-1, 1]:
        nt = t + x
        if nt in visited:
            continue
        visited.add(nt)
        res += cnt
        q.append([nt, cnt + 1])
        m += 1
        if m == k:
            print(res)
            exit()
    