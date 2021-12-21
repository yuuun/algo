n, m = map(int, input().split())
paths = []
for _ in range(m):
    paths.append(list(map(int, input().split())))
paths = sorted(paths, key=lambda x: x[2])

parents = [i for i in range(n + 1)]
def find_parent(x):
    if parents[x] != x:
        return find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

ans = 0
for a, b, c in paths:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += c
        last = c
print(ans - last)