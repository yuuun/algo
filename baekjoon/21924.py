n, m = map(int, input().split())
road = []
for _ in range(m):
    a, b, c = map(int, input().split())
    road.append([c, a, b])
road = sorted(road)

parent = [i for i in range(n + 1)]
def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y =  find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
cnt = 0
for c, a, b in road:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cnt += 1
    else:
        ans += c

if cnt == n - 1:
    print(ans)
else:
    print(-1)