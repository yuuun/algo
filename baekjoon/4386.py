n = int(input())
xys = []
for _ in range(n):
    xys.append(list(map(float, input().split())))
def calculate(first, second):
    return round(((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5, 2)

path = []
for x in range(n):
    for y in range(x + 1, n):
        path.append([x, y, calculate(xys[x], xys[y])])
path = sorted(path, key=lambda x: x[2])

parent = [i for i in range(n)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
for x, y, d in path:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        ans += d
print(ans)