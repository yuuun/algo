from collections import deque
n, m = map(int, input().split())

bridge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])

s, e = map(int, input().split())

def bfs(mid):
    global visited
    visited[s] = True
    q = deque()
    q.append(s)

    while q:
        start = q.popleft()
        if start == e:
            return True
        for ne, nc in bridge[start]:
            if visited[ne] == 0 and mid <= nc:
                q.append(ne)
                visited[ne] = True
    return False

low, high = 1, 1000000000
while low <= high:
    visited = [False for _ in range(n + 1)]
    mid = (low + high ) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)