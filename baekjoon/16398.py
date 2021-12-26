n = int(input())
paths = []

for i in range(n - 1):
    tmp = list(map(int, input().split()))
    for idx, j in enumerate(tmp[i + 1:]):
        paths.append([i, idx + i + 1, j])
input()
paths = sorted(paths, key=lambda x:x[2])
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def find_union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
for a, b, c in paths:
    if find_parent(a) != find_parent(b):
        find_union(a, b)
        ans += c
print(ans)