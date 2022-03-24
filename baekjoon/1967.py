import sys
sys.setrecursionlimit(10**9)
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append([b, d])
    tree[b].append([a, d])

def dfs(idx, weight):
    for b, d in tree[idx]:
        if dist[b] == -1:
            d += weight
            dist[b] = d
            dfs(b, d)

def init(idx):
    global dist, visited
    dist = [-1] * n
    visited = [False] * n
    dist[idx] = 0
    visited[idx] = True

init(0)
dfs(0, 0)
leaf_node = dist.index(max(dist))

init(leaf_node)
dfs(leaf_node, 0)
print(max(dist))