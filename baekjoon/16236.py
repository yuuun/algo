from collections import deque
n = int(input())
space = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        cur = [i, tmp.index(9)]

fish = 2
dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    eat = []
    queue = deque()
    queue.append((x, y, 0))
    