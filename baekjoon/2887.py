n = int(input())
dis = [list(map(int, input().split())) + [i] for i in range(n)]

edges = []
for i in range(3):
    dis = sorted(dis, key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(dis[j - 1][i] - dis[j][i]), dis[j - 1][3], dis[j][3]))

parent = [i for i in range(n)]
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    parent[y] = x

edges = sorted(edges, key=lambda x:x[0])
ans = 0
for d, x, y in edges:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        ans += d
print(ans)

'''메모리 초과
n = int(input())
dis = [list(map(int, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, min(abs(dis[i][0] - dis[j][0]), abs(dis[i][1] - dis[j][1]), abs(dis[i][2] - dis[j][2]))])
edges = sorted(edges, key=lambda x: x[2])

parent = [i for i in range(n)]
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    parent[y] = x

ans = 0
for a, b, d in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += d
print(ans)
'''