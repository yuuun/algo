from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    a = tmp[0]
    a -= 1
    for t in range(1, len(tmp) - 2, 2):
        b, d = tmp[t], tmp[t + 1]
        b -= 1
        tree[a].append([b, d])
        tree[b].append([a, d])
def bfs(idx):
    max_val, max_idx = 0, 0
    q = deque()
    q.append([idx, 0])
    
    visited = [False] * (n + 1)
    visited[idx] = True
    while q:
        cur, dist = q.popleft()
        for b, d in tree[cur]:
            if not visited[b]:
                visited[b] = True
                d += dist
                q.append([b, d])
                if max_val < d:
                    max_val = d
                    max_idx = b
                
    return max_val, max_idx
_, idx = bfs(0)
max_val, _ = bfs(idx)
print(max_val)