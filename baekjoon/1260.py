n, m, v = map(int, input().split())

t = n + 1
adj = [[0 for _ in range(t)] for _ in range(t)]
visited = [False for _ in range(t)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

def dfs(v):
    print(v, end =' ')
    visited[v] = True
    for i in range(1, t):
        if not visited[i] and adj[i][v] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = True
    while queue:
        v = queue.pop(0)
        print(v, end =' ')  
        for i in range(1, t):
            if not visited[i] and adj[i][v] == 1:
                queue.append(i)
                visited[i] = True

dfs(v)
print('')

visited = [False for _ in range(t)]
bfs(v)