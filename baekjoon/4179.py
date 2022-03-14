from collections import deque
r, c = map(int, input().split())
maps = []
jqueue,  fqueue = deque(), deque()
f_visited = [[0] * c for _ in range(r)]
j_visited = [[0] * c for _ in range(r)]

for i in range(r):
    tmp = list(input())
    for j, t in enumerate(tmp):
        if t == 'J':
            jqueue.append([i, j])

        elif t == 'F':
            fqueue.append([i, j])
    maps.append(tmp)

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs():
    while fqueue:
        x, y = fqueue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not f_visited[nx][ny] and maps[nx][ny] != '#':
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    fqueue.append([nx, ny])

    while jqueue:
        x, y = jqueue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not j_visited[nx][ny] and maps[nx][ny] != '#':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        jqueue.append([nx, ny])
            else:
                print(j_visited[x][y] + 1)
                return 
    print('IMPOSSIBLE')

bfs()