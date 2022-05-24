n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    if find_parent(x) != find_parent(y):
        union_parent(x, y)

ans = 0
maps = [list(map(int, input().split())) for _ in range(n)]
path = []
for x in range(1, n):
    for y in range(x + 1, n):
        if parent[x + 1] != parent[y + 1]:
            path.append([x + 1, y + 1, maps[x][y]])
path = sorted(path, key=lambda x: x[2])

ans = 0
candidate = []
for x, y, d in path:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        ans += d
        candidate.append([x, y])
print('{0} {1}'.format(ans, len(candidate)))
for can in candidate:
    print(' '.join(map(str, can)))