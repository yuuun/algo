n = int(input())
m  = int(input())

cost = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost.append([a, b, c])

cost = sorted(cost, key=lambda x: x[2])

parents = [i for i in range(n)]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find_parent(x):
    if parents[x] != x:
        return find_parent(parents[x])
    return parents[x]

ans = 0
for a, b, c in cost:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += c
print(ans)