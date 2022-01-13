n = int(input())
m = int(input())

parent = [i for  i in range(n)]
possible = [[-1] * n for _ in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a, b = parent[a], parent[b]
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, v in enumerate(tmp):
        if v == 1:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))
plan =  [p - 1 for p in plan]

res = []
for p in plan:
    res.append(find_parent(parent, p))

if len(set(res)) == 1:
    print('YES')
else:
    print('NO')