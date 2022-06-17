from collections import deque
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input()))

dic = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}
check = [[-1] * m for _ in range(n)] # 아직 확인 못함: -1, 탈출 성공: 0, 탈출 실패: 1

def fill_check(q, val):
    while q:
        x, y = q.popleft()
        check[x][y] = val

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[False] * m for _ in range(n)]
    tmp = deque([[x, y]])
    while q:
        x, y = q.popleft()
        dx, dy = dic[maps[x][y]]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == 0:
                fill_check(tmp, 0)
                return True
            if check[nx][ny] == 1:
                fill_check(tmp, 1)
                return False
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])
                tmp.append([nx, ny])
        else:
            fill_check(tmp, 0)
            return True
    fill_check(tmp, 1)
    return False

cnt = 0
for x in range(n):
    for y in range(m):
        if check[x][y] == -1:
            if bfs(x, y):
                cnt += 1
        elif check[x][y] == 0:
            cnt += 1

print(cnt)