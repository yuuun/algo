from heapq import heappop, heappush
n, m = map(int, input().split())
edges = []
maps = [[] for _ in range(n + 1)]
dis = [1e20] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append([b, c])
    maps[b].append([a, c])

def sol(start):
    q = []
    heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, c = heappop(q)
        if dis[c] < d:
            continue
        for v, w in maps[c]:
            cost = w + d
            if cost < dis[v]:
                dis[v] = cost
                heappush(q, (cost, v))
s, t = map(int, input().split())
sol(s)
print(dis[t])