n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dic = {0: 1, 1: 2, 2: 0}
rev_dic = {0: 2, 1: 0, 2: 1}

if maps[0][0] == 0:
    visited[0][0][0] = 1

for i, j in zip(range(1, n), range(n)):
    cur = maps[0][i]
    


'''
q.append([0, 0])
while q:
    x, y = q.popleft()
    for dx, dy in [[0, 1], [1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            q.append([nx, ny])
            t = maps[nx][ny]
            next = dic[t]
            rev = rev_dic[t]

            if visited[x][y][t] == visited[x][y][next]:
                visited[nx][ny][t] = max(visited[nx][ny][t], visited[x][y][rev] + 1)
                for k in range(3):
                    if k != rev:
                        visited[nx][ny][k] = visited[nx][ny][k]
            else:
                visited[nx][ny][t] = visited[x][y][t]

print(visited)

'''
