n, m = map(int, input().split())

adj = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(adj[x])