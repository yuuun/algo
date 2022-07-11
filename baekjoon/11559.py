from collections import deque

n, m = 12, 6
maps = []
for i in range(12):
    maps.append(list(input()))
ans = 0
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def remove_marble():
    visited = [[False] * m for _ in range(n)]
    isFlag = False
    remove_list = deque()
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != '.':
                visited[i][j] = True
                tmp = deque([[i, j]])
                q = deque([[i, j]])
                useless = deque([[i, j]])
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if maps[i][j] == maps[nx][ny]:
                                q.append([nx, ny])
                                tmp.append([nx, ny])
                            else:
                                useless.append([nx, ny])
                if len(tmp) > 3:
                    remove_list.extend(tmp)
                    isFlag = True
                while useless:
                    x, y = useless.popleft()
                    visited[x][y] = False
    
    while remove_list:
        x, y = remove_list.popleft()
        maps[x][y] = '.'

    return isFlag

def move_maps():
    for j in range(m):
        tmp = deque()
        for i in range(n):
            if maps[i][j] != '.':
                tmp.append(maps[i][j])
        
        for i in range(n - len(tmp)):
            maps[i][j] = '.'
        for i in range(n - len(tmp), n):
            maps[i][j] = tmp.popleft()
    return

while True:
    if not remove_marble():
        break
    
    ans += 1
    move_maps()
print(ans)