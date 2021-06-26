n = int(input())
m = int(input())
t = n + 1
adj = [[0 for _ in range(t)] for _ in range(t)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1
visited = [False for _ in range(t)]

cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in range(1, t):
        if not visited[i] and adj[i][v] == 1:
            dfs(i)


#dfs(1)
#print(cnt - 1)


def bfs(v):
    cnt = 0
    queue = [v]
    visited[v] = True
    while queue:
        v = queue.pop(0)
        for i in range(1, t):
            if not visited[i] and adj[i][v] == 1:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt
    
print(bfs(1))