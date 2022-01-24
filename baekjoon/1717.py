import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] =  find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union_parent(a, b)
    elif c == 1:

        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")