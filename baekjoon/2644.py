from collections import deque
n = int(input())
t = n + 1
sx, sy = map(int, input().split())
m = int(input())

inp = [[] for _ in range(t)]
info = [0] * t
q = deque()

for _ in range(m):
    x, y = map(int, input().split())
    inp[x].append(y)
    inp[y].append(x)

q.append(sx)
visited = []
while q:
    x = q.popleft()
    if x == sy:
        break
    
    visited.append(x)
    for i in inp[x]:
        if i not in visited:
            info[i] = info[x] + 1
            q.append(i)

if info[sy] == 0:
    print(-1)
else:
    print(info[sy])