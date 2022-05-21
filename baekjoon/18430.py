n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

if n == 1 or m == 1:
    print(0)
    exit()

def rightUp(x, y):
    return maps[x][y - 1] + maps[x + 1][y] + 2 * maps[x][y]

def rightDown(x, y):
    return maps[x - 1][y] + maps[x][y - 1] + 2 * maps[x][y]

def leftUp(x, y):
    return maps[x][y + 1] + maps[x + 1][y] + 2 * maps[x][y]

def leftDown(x, y):
    return maps[x - 1][y] + maps[x][y + 1] + 2 * maps[x][y]

visited = [[False] * m for _ in range(n)]
max_val = 0
def sol(x, y, cur):
    global max_val
    if y == m:
        y = 0
        x += 1
    if x == n:
        max_val = max(max_val, cur)
        return
    if not visited[x][y]:
        if x + 1 < n and y > 0 and not visited[x + 1][y] and not visited[x][y - 1]:
            visited[x][y] = True
            visited[x][y - 1] = True
            visited[x + 1][y] = True
            ncur = cur + rightUp(x, y)
            sol(x, y + 1, ncur)
            visited[x][y] = False
            visited[x][y - 1] = False
            visited[x + 1][y] = False
        if x > 0 and y > 0 and not visited[x - 1][y] and not visited[x][y - 1]:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y - 1] = True
            ncur = cur + rightDown(x, y)
            sol(x, y + 1, ncur)
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y - 1] = False
        if x + 1 < n and y + 1 < m and not visited[x + 1][y] and not visited[x][y + 1]:
            visited[x][y] = True
            visited[x][y + 1] = True
            visited[x + 1][y] = True
            ncur = cur + leftUp(x, y)
            sol(x, y + 1, ncur)
            visited[x][y] = False
            visited[x][y + 1] = False
            visited[x + 1][y] = False
        if x > 0 and y + 1 < m and not visited[x - 1][y] and not visited[x][y + 1]:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y + 1] = True
            ncur = cur + leftDown(x, y)
            sol(x, y + 1, ncur)
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y + 1] = False
    sol(x, y + 1, cur)
            
sol(0, 0, 0)
print(max_val)
