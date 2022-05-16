from collections import deque
r, c, k = map(int, input().split())
dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 위, 왼, 아래, 오른쪽
dic = {'U': 0, 'D': 2, 'L': 1, 'R': 3}
maps = []
for _ in range(r):
    maps.append(list(map(lambda x:dic[x], list(input()))))

if k == 0:
    q = deque()
    q.append([0, 0])
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        d = maps[x][y]
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
            q.append([nx, ny])
            visited[nx][ny] = True

    if visited[-1][-1]:
        print('Yes')
    else:
        print('No')
else:
    q = deque()
    q.append([0, 0, 0])
    # 0: 한 개도 안 씀, 1: 오른쪽 하나 씀, 2: 왼쪽 하나 씀, 3: 왼, 오른 다 씀
    visited = [[[False] * 4 for _ in range(c)] for _ in range(r)]
    visited[0][0][0] = True
    while q:
        x, y, k = q.popleft()
        d = maps[x][y]
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        # 이어서 할 경우
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny][k]:
            q.append([nx, ny, k])
            visited[nx][ny][k] = True

        # 왼쪽꺼 쓰지 않은 경우
        if k & 1 == 0:
            nk = k | 1
            nd = (d + 1) % 4
            nx, ny = x + dxy[nd][0], y + dxy[nd][1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny][nk]:
                q.append([nx, ny, nk])
                visited[nx][ny][nk] = True
        # 오른쪽 꺼 쓰지 않은 경우
        if k & 2 == 0:
            nk = k | 2
            nd = (d - 1) % 4
            nx, ny = x + dxy[nd][0], y + dxy[nd][1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny][nk]:
                q.append([nx, ny, nk])
                visited[nx][ny][nk] = True
    
    if set(visited[-1][-1]) == {False}:
        print('No')
    else:
        print('Yes')